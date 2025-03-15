document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ navbar.js loaded");

    const dropdown = document.querySelector(".dropdown");
    const dropdownContent = document.querySelector(".dropdown-content");

    if (dropdown && dropdownContent) {
        // Show dropdown on hover
        dropdown.addEventListener("mouseenter", function () {
            dropdownContent.style.display = "block";
        });

        // Hide dropdown when mouse leaves
        dropdown.addEventListener("mouseleave", function () {
            dropdownContent.style.display = "none";
        });

        // Toggle dropdown on click (persistent)
        dropdown.addEventListener("click", function (event) {
            event.preventDefault();
            dropdownContent.style.display = dropdownContent.style.display === "block" ? "none" : "block";
        });

        // Hide dropdown when clicking outside
        document.addEventListener("click", function (event) {
            if (!dropdown.contains(event.target)) {
                dropdownContent.style.display = "none";
            }
        });
    }
});
