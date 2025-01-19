$(".sidebar-menu a[href='" + window.location.href + "']").not('.baseUrl').addClass('active').closest("ul").addClass("open");


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

    if (swipeDistance < -swipeThreshold && sidebar.classList.contains('collapsed')) {
        sidebar.classList.remove('collapsed');
        navbar.classList.remove('expanded');
        mainContent.classList.remove('expanded');
    } else if (swipeDistance > swipeThreshold && !sidebar.classList.contains('collapsed')) {
        sidebar.classList.add('collapsed');
        navbar.classList.add('expanded');
        mainContent.classList.add('expanded');
    }
});