document.addEventListener("DOMContentLoaded", function () {
    console.log("navbar.js loaded successfully!");

    const courseTab = document.querySelector(".dropbtn");
    const dropdownContent = document.querySelector(".dropdown-content");

    if (courseTab && dropdownContent) {
        // Show dropdown on hover
        courseTab.addEventListener("mouseenter", function () {
            dropdownContent.classList.add("show");
        });

        // Persist dropdown on click
        courseTab.addEventListener("click", function (event) {
            event.preventDefault();
            dropdownContent.classList.toggle("persist");
        });

        // Hide dropdown when clicking outside
        document.addEventListener("click", function (event) {
            if (!courseTab.contains(event.target) && !dropdownContent.contains(event.target)) {
                dropdownContent.classList.remove("show", "persist");
            }
        });
    }
});

