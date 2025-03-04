const sidebar = document.getElementById('sidebar');
const navbar = document.getElementById('navbar');
const mainContent = document.getElementById('mainContent');
const toggleMenu = document.getElementById('toggleMenu');
const loadingOverlay = document.getElementById('loading');

// دکمه جمع‌شدن منو
toggleMenu.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
    navbar.classList.toggle('expanded');
    mainContent.classList.toggle('expanded');
});

// باز و بسته کردن زیرمنوها
const menuItems = document.querySelectorAll('.sidebar-menu > li > a');

menuItems.forEach(menuItem => {
    menuItem.addEventListener('click', function (event) {

        // event.preventDefault();

        menuItems.forEach(item => {
            if (item !== menuItem) {
                item.nextElementSibling?.classList.remove('open');
            }
        });

        const submenu = this.nextElementSibling;
        if (submenu && submenu.classList.contains('submenu')) {
            submenu.classList.toggle('open');
        }
    });
});

// باز و بسته کردن منو با کشیدن انگشت
let touchStartX = 0;
let touchEndX = 0;
const swipeThreshold = 50;

document.addEventListener('touchstart', (event) => {
    touchStartX = event.touches[0].clientX;
});

document.addEventListener('touchmove', (event) => {
    touchEndX = event.touches[0].clientX;
});

document.addEventListener('touchend', () => {
    const swipeDistance = touchEndX - touchStartX;

    if (swipeDistance < -swipeThreshold && sidebar.classList.contains('collapsed') && 0) {
        sidebar.classList.remove('collapsed');
        navbar.classList.remove('expanded');
        mainContent.classList.remove('expanded');
    } else if (swipeDistance > swipeThreshold && !sidebar.classList.contains('collapsed')) {
        sidebar.classList.add('collapsed');
        navbar.classList.add('expanded');
        mainContent.classList.add('expanded');
    }
});


$(document).on("change", ".checkboxLable input[type='checkbox']", function () {
    if ($(this).is(":checked")) {
        $(this).next('i')
            .addClass('fa-check').removeClass('fa-times')
            .closest('label').addClass('bg-info').removeClass('bg-secondary')
    }
    else {
        $(this).next('i')
            .removeClass('fa-check').addClass('fa-times')
            .closest('label').removeClass('bg-info').addClass('bg-secondary')
    }
})

// $(document).on("keyup", "input , textarea", function (e) {
//     var key = e.which || e.keyCode || 0;
//     // console.log(key)
//     if (e.ctrlKey && key == 83) {
//         $(this).closest("form:not(.ajaxform)").submit()
//     }
// })