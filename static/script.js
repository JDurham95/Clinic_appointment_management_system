document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("button.add")?.addEventListener("click", (event) => {
        document.querySelector(".add-form-popup").classList.add("active");
    });

    document.querySelector("button.close").addEventListener("click", (event) => {
        document.querySelector(".add-form-popup").classList.remove("active");
        window.location.href = window.location.href.split("?").slice(0, -1).toString()
    });

    document.querySelectorAll('.delete-trigger').forEach(button => {
        button.addEventListener('click', function(e) {
            const testId = this.getAttribute('data-id');
            document.getElementById('deleteId').value = testId;
            document.querySelector('.delete-form-popup').classList.add('active');
        });
    });

    document.getElementById('cancel').addEventListener('click', function() {
        document.querySelector('.delete-form-popup').classList.remove('active');
    });

    document.querySelector(".reset-trigger").addEventListener("click", () => {
        document.querySelector('.reset-form-popup').classList.add('active');
    });

    document.querySelector('.cancel').addEventListener('click', function() {
        document.querySelector('.reset-form-popup').classList.remove('active');
    });

    // document.querySelector("button.submit").addEventListener("click", (event) =>{
    //     event.preventDefault();
    //     document.querySelector(".add-form-popup form").submit();
    // });
});