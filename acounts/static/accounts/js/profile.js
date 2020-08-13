// ================== Dropdown-menu-Profile ===============================*/
/////////////////////////////////////////////////////////////////////////////
  /* When the user clicks on the button,toggle between hiding and showing the dropdown content */
  function myFunc() {
    document.getElementById("id01").classList.toggle("show");
  }
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbttn')) {
      var dropdowns = document.getElementsByClassName("dropdown-menu");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
  /* When the user clicks on the button, toggle between hiding and showing the dropdown content for mobile screen*/
  function myFunct() {
    document.getElementById("id02").classList.toggle("show");
  }
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbttn-mobile')) {
      var dropdowns = document.getElementsByClassName("dropdown-menu-mobile");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

//============================ FlipCard-Profile-content =======================
///////////////////////////////////////////////////////////////////////////////
function openCardContent(evt, card1, card2) {
  var i, tabcontent, tablinks;
  tabcontent = document.querySelectorAll("div.card-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("ic-profile-menu");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  // document.querySelectorAll("div.card-content")
  document.getElementById(card1).style.display = "block";
  document.getElementById(card2).style.display = "block";
  evt.currentTarget.className += " active";
}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
//=========================== NewObject of card-Profile =======================
///////////////////////////////////////////////////////////////////////////////
  /* When the user clicks on the button, toggle between hiding and showing the dropdown content for mobile screen
  function newCreate() {
    document.getElementById("project01").classList.toggle("show");
  }
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.createBtb')) {
      var dropdowns = document.getElementsByClassName("create-doc-projec");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }
  */
  // Get the modal for button 1
function MyFuncOpen(open) {
  open = document.getElementById('project01').style.display='block'
}

// When the user clicks anywhere outside of the modal, close it
function MyFuncClose(close) {
  close = document.getElementById('project01').style.display='none'
}