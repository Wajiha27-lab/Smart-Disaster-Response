// Smart Disaster Response - Frontend JavaScript

document.addEventListener("DOMContentLoaded", function () {
    console.log("Smart Disaster Response loaded.");
});

function validateForm() {
    const location = document.querySelector("input[name='location']").value.trim();
    const report = document.querySelector("textarea[name='report']").value.trim();

    if (location === "" || report === "") {
        alert("Please enter both the location and the disaster report.");
        return false;
    }

    return true;
}

function previewImage(input) {
    const preview = document.getElementById("imagePreview");

    if (!preview || !input.files || !input.files[0]) {
        return;
    }

    const reader = new FileReader();

    reader.onload = function (e) {
        preview.src = e.target.result;
        preview.style.display = "block";
    };

    reader.readAsDataURL(input.files[0]);
}
