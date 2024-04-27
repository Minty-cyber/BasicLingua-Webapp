window.onload = function() {
    var cachedApiKey = localStorage.getItem("api_key");
    var cachedUserInput = localStorage.getItem("user_input");
    var cachedMode = localStorage.getItem("mode");
    

    document.getElementById("api_key").value = cachedApiKey || "";
    document.getElementById("user_input").value = cachedUserInput && "";
    document.getElementById("mode").value = cachedMode && "";
};



document.getElementById("summarize-button").addEventListener("click", function() {
    var apiKey = document.getElementById("api_key").value.trim();
    var userInput = document.getElementById("user_input").value.trim();
    var patterns = document.getElementById("mode").value.trim();

    if (apiKey === "" || userInput === "" || mode === "") {
        alert("Please fill in all required fields.");
        return;
    }

    document.getElementById("loader").style.display = "block";

    localStorage.setItem("api_key", apiKey);
    localStorage.setItem("user_input", userInput);
    localStorage.setItem("summary_length", patterns);

    $.ajax({
        url: translationUrl,
        type: "POST",
        data: $("#translation-form").serialize(),
        success: function(response) {
            document.getElementById("loader").style.display = "none";
            console.log("Response:", response);
            document.getElementById("summary-result").innerHTML = "<h4>Summarized Text</h4><p style='text-align: left; max-width: 100%; overflow-wrap: break-word;'>" + response.summary + "</p>";
        },
        error: function(xhr, errmsg, err) {
            document.getElementById("loader").style.display = "none";
            document.getElementById("summary-result").innerHTML = "<h4>Error retrieving output</h4><p style='text-align: left;'>" + xhr.status + "</p>";
            console.log("Error:", xhr.status);
        }
    });
});

document.getElementById("refresh-button").addEventListener("click", function() {
    document.getElementById("user_input").value = "";
    document.getElementById("summary_length").value = "";
    document.getElementById("summary-result").innerHTML = "";

    
    localStorage.removeItem("user_input");
    localStorage.removeItem("summary_length");
});
