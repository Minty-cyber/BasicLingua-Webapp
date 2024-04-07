window.onload = function() {
    var cachedApiKey = localStorage.getItem("api_key");
    var cachedUserInput = localStorage.getItem("user_input");
    var cachedAnswerLength = localStorage.getItem("ans_length");
    

    document.getElementById("api_key").value = cachedApiKey || "";
    document.getElementById("user_input").value = cachedUserInput && "";
    document.getElementById("ans_length").value = cachedAnswerLength && "";
};



document.getElementById("answer-button").addEventListener("click", function() {
    var apiKey = document.getElementById("api_key").value.trim();
    var userInput = document.getElementById("user_input").value.trim();
    var answerLength = document.getElementById("ans_length").value.trim();

    if (apiKey === "" || userInput === "" || answerLength === "") {
        alert("Please fill in all required fields.");
        return;
    }

    document.getElementById("loader").style.display = "block";

    localStorage.setItem("api_key", apiKey);
    localStorage.setItem("user_input", userInput);
    localStorage.setItem("ans_length", taskType);

    $.ajax({
        url: translationUrl,
        type: "POST",
        data: $("#translation-form").serialize(),
        success: function(response) {
            document.getElementById("loader").style.display = "none";
            console.log("Response:", response);
            document.getElementById("answer-result").innerHTML = "<h4>Answer</h4><p style='text-align: left; max-width: 100%; overflow-wrap: break-word;'>" + response.answer + "</p>";
        },
        error: function(xhr, errmsg, err) {
            document.getElementById("loader").style.display = "none";
            document.getElementById("answer-result").innerHTML = "<h4>Error retrieving output</h4><p style='text-align: left;'>" + xhr.status + "</p>";
            console.log("Error:", xhr.status);
        }
    });
});

document.getElementById("refresh-button").addEventListener("click", function() {
    document.getElementById("user_input").value = "";
    document.getElementById("ans_length").value = "";
    document.getElementById("answer-result").innerHTML = "";

    
    localStorage.removeItem("user_input");
    localStorage.removeItem("task_type");
});


