// const theme = localStorage.getItem("theme") || "light";
    // document.body.classList.add(theme + "-theme");

    const sidebar = document.getElementById('sidebar');
    const hamburger = document.getElementById('hamburger');
    const themeToggle = document.querySelector('.theme-toggle');

    hamburger.addEventListener('mouseenter', openNav);
    sidebar.addEventListener('mouseleave', closeNav);

    function openNav() {
        sidebar.style.width = '200px';
        hamburger.style.display = 'none';
    }

    function closeNav() {
        sidebar.style.width = '0';
        hamburger.style.display = 'block';
    }

    // function toggleTheme() {
    //     const currentTheme = document.body.classList.contains("dark-theme") ? "dark" : "light";
    //     const newTheme = currentTheme === "dark" ? "light" : "dark";
        
    //     // Toggle theme class
    //     localStorage.setItem("theme", newTheme);
    //     document.body.classList.remove(currentTheme + "-theme");
    //     document.body.classList.add(newTheme + "-theme");
    // }