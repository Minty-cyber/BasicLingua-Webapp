window.onload = function() {
    var cachedApiKey = localStorage.getItem("api_key");
    var cachedUserInput = localStorage.getItem("user_input");
    var cachedSummaryLength = localStorage.getItem("summary_length");
    

    document.getElementById("api_key").value = cachedApiKey || "";
    document.getElementById("user_input").value = cachedUserInput && "";
    document.getElementById("ner_tags").value = cachedTargetLang && "";
};



document.getElementById("extract-button").addEventListener("click", function() {
    var apiKey = document.getElementById("api_key").value.trim();
    var userInput = document.getElementById("user_input").value.trim();
    var patterns = document.getElementById("ner_tags").value.trim();

    if (apiKey === "" || userInput === "" || ner_tags === "") {
        alert("Please fill in all required fields.");
        return;
    }

    document.getElementById("loader").style.display = "block";

    localStorage.setItem("api_key", apiKey);
    localStorage.setItem("user_input", userInput);
    localStorage.setItem("ner_tags", patterns);

    $.ajax({
        url: translationUrl,
        type: "POST",
        data: $("#translation-form").serialize(),
        success: function(response) {
            document.getElementById("loader").style.display = "none";
            console.log("Response:", response);
            document.getElementById("extraction-result").innerHTML = "<h4>Extraction Result</h4><p style='text-align: left; max-width: 100%; overflow-wrap: break-word;'>" + response.answer + "</p>";
        },
        error: function(xhr, errmsg, err) {
            document.getElementById("loader").style.display = "none";
            document.getElementById("extraction-result").innerHTML = "<h4>Error retrieving output</h4><p style='text-align: left;'>" + xhr.status + "</p>";
            console.log("Error:", xhr.status);
        }
    });
});

document.getElementById("refresh-button").addEventListener("click", function() {
    document.getElementById("user_input").value = "";
    document.getElementById("ner_tags").value = "";
    document.getElementById("extraction-result").innerHTML = "";

    
    localStorage.removeItem("user_input");
    localStorage.removeItem("ner_tags");
});
