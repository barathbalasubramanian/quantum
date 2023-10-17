
document.addEventListener('DOMContentLoaded', function() {
    const photoDiv = document.querySelector('.photo');
    const cardDiv = document.querySelector('.card');
    const closeButton = document.querySelector('.close-btn');

    photoDiv.addEventListener('click', function() {
        cardDiv.style.display = 'flex'; // Show the card
    });

    closeButton.addEventListener('click', function() {
        cardDiv.style.display = 'none'; // Hide the card
    });



    const imageInput = document.getElementById('imageInput');
    const triggerButton = document.getElementById('triggerInput');
    const previewImage = document.getElementById('previewImage');
    const openCamButton = document.querySelector('.open-cam.btn');
    const uploadButtonDiv = document.querySelector('.upload-btn.btn');
    const submitButtonDiv = document.querySelector('.submit-btn.btn');

    triggerButton.addEventListener('click', function() {
        imageInput.click();
    });

    imageInput.addEventListener('change', function() {
        if (imageInput.files.length) {
            previewImage.src = URL.createObjectURL(imageInput.files[0]);
            openCamButton.style.display = 'none';
            uploadButtonDiv.style.display = 'none';
            submitButtonDiv.style.display = 'block';
        }
    });

    document.getElementById('submitButton').addEventListener('click', function() {
        console.log("Submit Button Clicked");
    });

});




