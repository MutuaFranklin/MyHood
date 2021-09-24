



// Profile
function showPosts() {
    document.getElementById("posts").style.display = " block";
    document.getElementById("posts").style.display = " flex";  
    document.getElementById("business").style.display = "none"; 
    document.getElementById("neighbors").style.display = "none";


}
// show business hide  posts and neighbors
function showBusiness() {
    document.getElementById("business").style.display = " block";
    document.getElementById("posts").style.display = "none";
    document.getElementById("neighbors").style.display = "none";



}

function showNeighbors() {
  document.getElementById("neighbors").style.display = " block";
  document.getElementById("posts").style.display = "none";
  document.getElementById("business").style.display = "none";


}

