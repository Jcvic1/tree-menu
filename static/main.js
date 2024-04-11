document.addEventListener('DOMContentLoaded', function () {
    var currentPath = window.location.pathname;

    var menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(function (item) {
        var submenu = item.querySelector('.submenu');
        var textBtn = item.querySelector('.text-btn');
        var url = item.getAttribute('data-url');


        var toggleBtn = item.querySelector('.toggle-btn');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', function (event) {
                event.stopPropagation();
                submenu.classList.toggle('expanded');
                if (toggleBtn.classList.contains("bi-plus-circle")) {
                    toggleBtn.classList.remove("bi-plus-circle");
                    toggleBtn.classList.add("bi-dash-circle");
                } else {
                    toggleBtn.classList.remove("bi-dash-circle");
                    toggleBtn.classList.add("bi-plus-circle");
                }
                if (toggleBtn.classList.contains("text-primary")) {
                    toggleBtn.classList.remove("text-primary");
                    toggleBtn.classList.add("text-light");
                } else {
                    toggleBtn.classList.remove("text-light");
                    toggleBtn.classList.add("text-primary");
                }
            });
        }

        textBtn.addEventListener('click', function (event) {
            event.preventDefault();
            window.location.href = url;
        });

        if (currentPath === url) {
            textBtn.classList.add('active');
            expandParents(item);
        }
    });

    function expandParents(item) {
        var parent = item.closest('.menu-item');

        if (parent) {
            var submenu = parent.closest('.submenu');
            if (submenu && !submenu.classList.contains('expanded')) {
                submenu.classList.add('expanded');
                expandParents(submenu);
            }

        }



    }
});