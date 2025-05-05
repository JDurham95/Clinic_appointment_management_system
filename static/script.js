document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("button.add")?.addEventListener("click", (event) => {
        document.querySelector(".add-form-popup").classList.add("active");
    });

    document.querySelector("button.close").addEventListener("click", (event) => {
        console.log("here")
        document.querySelector(".add-form-popup").classList.remove("active");
        window.location.href = window.location.href.split("?").slice(0, -1).toString()
    });

    document.querySelector("button.submit").addEventListener("click", (event) =>{
        event.preventDefault();
        document.querySelector(".add-form-popup form").submit();
    });
});