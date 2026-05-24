function loadJobs() {
    fetch("/api/jobs/")
        .then(res => res.json())
        .then(data => {
            let container = document.getElementById("jobList");
            container.innerHTML = "";

            if (data.length === 0) {
                container.innerHTML = "<p>No jobs available</p>";
                return;
            }

            data.forEach(job => {
                container.innerHTML += `
                    <div class="job-card">
                        <h3>${job.title}</h3>
                        <p><b>Skills:</b> ${job.required_skills}</p>
                    </div>
                `;
            });
        })
        .catch(error => {
            console.log("Error loading jobs:", error);
            document.getElementById("jobList").innerHTML =
                "<p>Failed to load jobs</p>";
        });
}

function loadCandidates() {
    fetch("/api/candidates/")
        .then(res => res.json())
        .then(data => {
            data.sort((a, b) => b.score - a.score);
            let container = document.getElementById("candidateList");
            container.innerHTML = "";
            if (data.length === 0) {
                container.innerHTML = "<p>No candidates available</p>";
                return;
            }

            data.forEach(candidate => {
                container.innerHTML += `
                    <div class="job-card">

                        <h3>${candidate.candidate_name}</h3>

                        <p><b>Email:</b> ${candidate.email}</p>

                        <p><b>Skills:</b> ${candidate.candidate_skills}</p>

                        <p><b>Applied Job:</b> ${
                            candidate.applied_job?.title || "N/A"
                        }</p>

                        <p><b>ATS Score:</b> ${candidate.score ?? "Not calculated"}</p>

                    </div>
                `;
            });
        })
        .catch(error => {
            console.log("Error loading candidates:", error);
            document.getElementById("candidateList").innerHTML =
                "<p>Failed to load candidates</p>";
        });
}