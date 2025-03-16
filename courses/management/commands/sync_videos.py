import os
import datetime
import ffmpeg  # Install with `pip install ffmpeg-python`
from django.core.management.base import BaseCommand
from django.conf import settings
from courses.models import Course, Video

class Command(BaseCommand):
    help = "Sync videos from the local directory to the database."

    def handle(self, *args, **options):
        # ✅ Define the correct video root directory
        video_root = os.path.join(settings.BASE_DIR, "videos")  # Ensure this matches your project structure

        if not os.path.exists(video_root):
            self.stdout.write(self.style.ERROR(f"⚠️ Video root directory {video_root} does not exist."))
            return

        self.stdout.write(self.style.SUCCESS(f"📂 Scanning video root directory: {video_root}"))

        # ✅ Iterate through course directories
        for course_folder in sorted(os.listdir(video_root)):  # Ensure consistent order
            course_path = os.path.join(video_root, course_folder)

            if not os.path.isdir(course_path):
                continue  # Skip non-directory files

            # Find or create a Course
            course, created = Course.objects.get_or_create(
                title=course_folder,
                defaults={"display_name": course_folder}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Created new course: {course_folder}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Course exists: {course_folder}"))

            # ✅ Iterate through video files in the course folder
            video_files = sorted(
                [f for f in os.listdir(course_path) if f.lower().endswith((".mp4", ".avi", ".mov", ".mkv"))]
            )

            for index, filename in enumerate(video_files, start=1):  # Assign `video_order`
                video_path = os.path.join(course_path, filename)

                # Extract video metadata
                display_name = os.path.splitext(filename)[0]
                duration = self.get_video_duration(video_path)

                # Add or update the video in the database
                video, created = Video.objects.update_or_create(
                    course=course,
                    title=filename,
                    defaults={
                        "display_name": display_name,
                        "duration": duration,
                        "video_url": f"/videos/{course_folder}/{filename}",  # Static serving URL
                        "video_order": index,  # ✅ Assign video order correctly
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"✅ Added video: {filename} (~{duration} mins, Order {index})"))
                else:
                    self.stdout.write(self.style.WARNING(f"⚠️ Updated video: {filename} (~{duration} mins, Order {index})"))

        self.stdout.write(self.style.SUCCESS("🎉 Video sync completed successfully!"))

    def get_video_duration(self, video_path):
        """Extract the duration of a video file using ffmpeg and return in rounded minutes."""
        try:
            probe = ffmpeg.probe(video_path)
            duration_seconds = float(probe["format"]["duration"])  # Get total duration in seconds
            duration_minutes = round(duration_seconds / 60)  # Convert to minutes and round

            return f"{duration_minutes} mins"  # ✅ Fix: Ensure only one `~`
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Failed to get duration for {video_path}: {e}"))
            return "~30 mins"  # Default fallback duration