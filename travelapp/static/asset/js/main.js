document.addEventListener('DOMContentLoaded', function() {
  const listItems = document.querySelectorAll(".sidebar-list li");

  listItems.forEach((item) => {
      item.addEventListener("click", () => {
          let isActive = item.classList.contains("active");

          listItems.forEach((el) => {
              el.classList.remove("active");
          });

          if (isActive) item.classList.remove("active");
          else item.classList.add("active");
      });
  });

  const toggleSidebar = document.querySelector(".toggle-sidebar");
  const logo = document.querySelector(".logo-box");
  const sidebar = document.querySelector(".sidebar");

  if (toggleSidebar) {
      toggleSidebar.addEventListener("click", () => {
          sidebar.classList.toggle("close");
      });
  }

  if (logo) {
      logo.addEventListener("click", () => {
          sidebar.classList.toggle("close");
      });
  }
});
