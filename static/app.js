// JOBS PAGE
if (document.getElementById("jobList")) {

    fetch("https://rohit7709.pythonanywhere.com/api/jobs/")
    .then(response => response.json())
    .then(data => {

        let output = "";

        data.forEach(job => {

            output += `
                <div class="card">
                    <h2>${job.title}</h2>
                    <p><b>Skills:</b> ${job.required_skills}</p>
                    <p><b>Created:</b> ${job.created_time}</p>
                </div>
            `;

        });

        document.getElementById("jobList").innerHTML = output;

    })
    .catch(error => console.log("Jobs Error:", error));
}



// CANDIDATES PAGE
if (document.getElementById("candidateList")) {

    fetch("https://rohit7709.pythonanywhere.com/api/candidates/")
    .then(response => response.json())
    .then(data => {

        let output = "";

        data.forEach(candidate => {

            output += `
                <div class="card">
                    <h2>${candidate.candidate_name}</h2>
                    <p><b>Email:</b> ${candidate.email}</p>
                    <p><b>Skills:</b> ${candidate.candidate_skills}</p>
                    <p><b>ATS Score:</b> ${candidate.score}%</p>
                </div>
            `;

        });

        document.getElementById("candidateList").innerHTML = output;

    })
    .catch(error => console.log("Candidates Error:", error));
}



// NOTIFICATIONS PAGE
if (document.getElementById("notificationList")) {

    fetch("https://rohit7709.pythonanywhere.com/api/notifications/")
    .then(response => response.json())
    .then(data => {

        let output = "";

        data.forEach(notification => {

            output += `
                <div class="card">
                    <h3>${notification.message}</h3>
                    <p><b>Status:</b> ${notification.is_read ? "Read" : "Unread"}</p>
                    <p><b>Time:</b> ${notification.created_at}</p>
                </div>
            `;

        });

        document.getElementById("notificationList").innerHTML = output;

    })
    .catch(error => console.log("Notifications Error:", error));
}



// LOGIN FUNCTION
function login(){

    const username = document.getElementById("username").value;

    const password = document.getElementById("password").value;

    if(username === "rohit" && password === "rohit12@"){

        window.location.href = "/api/jobs/";

    }

    else{

        alert("Invalid Credentials");

    }


}