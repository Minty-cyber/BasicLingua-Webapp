const sidebar = document.getElementById('sidebar');
const hamburger = document.getElementById('hamburger');

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

document.getElementById("api_key_input").value = localStorage.getItem("api_key") || "";

document.getElementById("api-key-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var apiKey = document.getElementById("api_key_input").value;
    localStorage.setItem("api_key", apiKey); 
    
    document.getElementById("message").innerHTML = "API key saved!"; 
    document.getElementById("message").style.display = "block"; 

    setTimeout(function() {
        document.getElementById("message").style.opacity = "0";
        setTimeout(function() {
            document.getElementById("message").style.display = "none";
        }, 1000);
    }, 3000); 
    

});

document.getElementById("clear-cache-button").addEventListener("click", function(event) {
    event.preventDefault();
    localStorage.removeItem("api_key");
    document.getElementById("api_key_input").value = "";
    document.getElementById("message").innerHTML = "API key cleared from cache!";
    document.getElementById("message").style.display = "block"; 

    setTimeout(function() {
        document.getElementById("message").style.opacity = "0";
        setTimeout(function() {
            document.getElementById("message").style.display = "none";
        }, 1000);
    }, 3000);
});

    document.querySelector('a[href="{% url "text-translation" %}"]').addEventListener("click", function(event) {
    if (!document.getElementById("api_key_input").value.trim()) {
        event.preventDefault();
        alert("Please enter your API key before accessing the Text Translation feature!");
    }
});

document.querySelector('a[href="{% url "text-replace" %}"]').addEventListener("click", function(event) {
    if (!document.getElementById("api_key_input").value.trim()) {
        event.preventDefault();
        alert("Please enter your API key before accessing the Text Replace feature!");
    }
});

document.querySelector('a[href="{% url "text-correction" %}"]').addEventListener("click", function(event) {
    if (!document.getElementById("api_key_input").value.trim()) {
        event.preventDefault();
        alert("Please enter your API key before accessing the Text Correction feature!");
    }
});

document.querySelector('a[href="{% url "extract-patterns" %}"]').addEventListener("click", function(event) {
    if (!document.getElementById("api_key_input").value.trim()) {
        event.preventDefault();
        alert("Please enter your API key before accessing the Extract Patterns feature!");
    }
});