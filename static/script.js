/* 
Clinic Appointment Management System script.js
Fidella Wu, Jacob Durham
CS340 - Introduction to Databases Spring 2025

Citations: 

Citation for JS event listeners used for clicking on buttons 
Scope: Function
Originality: Adapted
Source URL: https://www.w3schools.com/js/js_htmldom_eventlistener.asp
Date: 5/3/2025

Citation for JS window location
Scope: Function
Originality: Adapted
Source URL: https://www.w3schools.com/js/js_window_location.asp
Date: 5/4/2025

Citation for JS Split and Slice
Scope: Line, 38
Originality: Adapted
Source URL: https://www.w3schools.com/jsref/jsref_split.asp
Source URL: https://www.w3schools.com/jsref/jsref_slice_string.asp
Date: 5/4/2025 
*/

document.addEventListener("DOMContentLoaded", function () {
    // Show the add form when the add button is clicked
    document.querySelector("button.add")?.addEventListener("click", (event) => {
        document.querySelector(".add-form-popup").classList.add("active");
    });

    // Close the add/update form when the close button/x is clicked
    document.querySelector("button.close")?.addEventListener("click", (event) => {
        document.querySelector(".add-form-popup").classList.remove("active");
        // Update url so that the query parameter (?) from the update form is not part of the URL
        window.location.href = window.location.href.split("?").slice(0, -1).toString();
    });

    // Show delete popup when delete button is clicked
    document.querySelectorAll('.delete-trigger').forEach(button => {
        button.addEventListener('click', function(e) {
            // Use data attributes to determine which item to delete
            const dataId = this.getAttribute('data-id');
            document.getElementById('deleteId').value = dataId;
            document.querySelector('.delete-form-popup').classList.add('active');
        });
    });

    // Close delete popup when the cancel button is clicked
    document.getElementById('cancel')?.addEventListener('click', function() {
        document.querySelector('.delete-form-popup').classList.remove('active');
    });

    // Show the reset popup when the reset button on the navigation is clicked
    document.querySelector(".reset-trigger").addEventListener("click", () => {
        document.querySelector('.reset-popup').classList.add('active');
    });

    // Close the reset form when the cancel button is clicked
    document.querySelector('.cancel').addEventListener('click', function() {
        document.querySelector('.reset-popup').classList.remove('active');
    });
});