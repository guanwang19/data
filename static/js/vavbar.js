document.addEventListener("DOMContentLoaded", function () {
    let dropdown = document.querySelector(".dropbtn");
    let dropdownContent = document.querySelector(".dropdown-content");

    dropdown.addEventListener("click", function (event) {
        event.preventDefault();
        dropdownContent.style.display = dropdownContent.style.display === "block" ? "none" : "block";
    });

    document.addEventListener("click", function (event) {
        if (!dropdown.contains(event.target)) {
            dropdownContent.style.display = "none";
        }
    });
});
