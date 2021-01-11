// // function myFunction() {
var navBtn = document.getElementById("navBtn");
var bigNav = document.getElementById("bigNav");
var dropdownlist = document.getElementById("dropdownlist");
var mainNav = document.getElementById("mainNav");
var nav = document.getElementById("nav");
var searchForm = document.getElementById("searchForm");
var selectForm = document.getElementById("selectForm");
// nav bar responsive
if (window.innerWidth > 768) {
  dropdownlist.appendChild(bigNav);
  bigNav.style.display = "block";
} else {
  bigNav.style.display = "none";
}

navBtn.addEventListener("click", function () {
  if (!navBtn.classList.contains("click")) {
    navBtn.innerHTML = '<i class="far fa-times-circle"></i>';
    bigNav.style.display = "block";
    navBtn.classList.add("click");
  } else {
    navBtn.innerHTML = '<i class="fas fa-ellipsis-h"></i>';
    bigNav.style.display = "none";
    navBtn.classList.remove("click");
  }
});

function reSize() {
  if (window.innerWidth > 768) {
    navBtn.style.display = "none";
    dropdownlist.appendChild(bigNav);
    bigNav.style.display = "block";
  } else {
    navBtn.style.display = "block";
    mainNav.appendChild(bigNav);

    if (!navBtn.classList.contains("click")) {
      bigNav.style.display = "none";
    } else {
      bigNav.style.display = "block";
    }
  }
}

// nav bar fix top
window.addEventListener("scroll", function () {
  var position = window.innerHeight;
  if (position > 0) {
    nav.classList.add("fixtop");
  }
});

//star rating
$(document).ready(function () {
  $("label").click(function () {
    $("label").removeClass("active");
    $(this).addClass("active");
  });
});

// // }
