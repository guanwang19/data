from django.core.management.base import BaseCommand
import os
import random
from datetime import timedelta
from django.utils.timezone import now
from django.conf import settings
from courses.models import Course, Video


VIDEO_DIR = os.path.join(settings.BASE_DIR, "videos")


class Command(BaseCommand):
    help = "Syncs the database with video files in /videos/"

    def handle(self, *args, **kwargs):
        """Main method executed when running the command"""
        self.sync_videos()

    def sync_videos(self):
        """
        - Adds new courses if a subfolder exists
        - Adds new videos
        - Marks missing videos as Inactive instead of deleting
        - Keeps existing descriptions and display names
        - Updates course statistics
        """
        if not os.path.exists(VIDEO_DIR):
            self.stdout.write(self.style.WARNING(f"⚠️ Video directory {VIDEO_DIR} does not exist."))
            return

        found_courses = set()
        found_videos = set()

        self.stdout.write("🔄 Syncing videos...")

        # ✅ Scan subdirectories (each representing a course)
        for course_folder in sorted(os.listdir(VIDEO_DIR)):
            course_path = os.path.join(VIDEO_DIR, course_folder)

            if not os.path.isdir(course_path):
                continue  # Skip non-directory files

            # ✅ Ensure the course exists in the database
            course, created = Course.objects.get_or_create(
                title=course_folder,
                defaults={
                    "display_name": course_folder,  # ✅ Set display name as folder name initially
                    "description": f"Auto-created for {course_folder}",
                }
            )
            found_courses.add(course.id)

            if created:
                self.stdout.write(self.style.SUCCESS(f"🆕 Created course: {course.display_name}"))

            self.stdout.write(f"📂 Processing course: {course.display_name}")

            # ✅ Scan video files
            video_files = sorted([f for f in os.listdir(course_path) if f.endswith(('.mp4', '.mov', '.avi'))])

            for index, filename in enumerate(video_files, start=1):
                video_path = os.path.join(course_path, filename)
                video_url = f"/videos/{course_folder}/{filename}"

                # ✅ Ensure the video exists in the database
                video, created = Video.objects.get_or_create(
                    course=course,
                    title=filename,  # ✅ Store filename as title
                    video_order=index,
                    defaults={
                        "display_name": os.path.splitext(filename)[0],  # ✅ Set display_name initially
                        "duration": timedelta(minutes=random.randint(5, 20)),  # Placeholder duration
                        "video_url": video_url,
                        "status": "Active",
                        "access_type": "Restricted",
                        "author": "James",
                        "added_at": now(),
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"🎥 Added video: {video.display_name} (Order: {video.video_order})"))
                else:
                    video.status = "Active"
                    video.video_url = video_url
                    video.save()
                    self.stdout.write(self.style.SUCCESS(f"✅ Updated video: {video.display_name} (Order: {video.video_order})"))

                found_videos.add(video.id)

            # ✅ Mark missing videos as Inactive
            existing_videos = Video.objects.filter(course=course, status="Active")
            for vid in existing_videos:
                if vid.id not in found_videos:
                    vid.status = "Inactive"
                    vid.save()
                    self.stdout.write(self.style.WARNING(f"⚠️ Marked Inactive: {vid.display_name}"))

            # ✅ Update course stats
            course.update_video_stats()
            self.stdout.write(self.style.SUCCESS(f"📊 Updated Course Stats: {course.display_name} - {course.total_videos} Videos"))

        self.stdout.write(self.style.SUCCESS("✅ Video sync completed!"))
