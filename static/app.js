fetch("https://rohit7709.pythonanywhere.com/api/jobs/")
.then(response => response.json())
.then(data => {

    let output = "";

    data.forEach(job => {
        output += `
            <div>
                <h3>${job.title}</h3>
                <p>${job.required_skills}</p>
            </div>
        `;
    });

    document.getElementById("jobList").innerHTML = output;
});