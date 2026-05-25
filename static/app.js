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

console.log("JS FILE LOADED");
function loadCandidates() {
                    console.log("FUNCTION CALLED");

    fetch("/api/candidates/")
        .then(res => res.json())
        .then(data => {

             console.log("before sorted Sort:", data);
             data.sort((a, b) =>
                Number(b.score || 0) - Number(a.score || 0));
             console.log('sorted data',data)

            let container = document.getElementById("candidateList");

            container.innerHTML = "";

            if (data.length === 0) {
                container.innerHTML = "<p>No candidates available</p>";
                return;
            }

            let html = "";

            data.forEach(candidate => {

                html += `
                  <div class="candidate-row">

        <div class="col">
            ${candidate.candidate_name}
        </div>

        <div class="col">
            ${candidate.email}
        </div>

        <div class="col">
            ${candidate.candidate_skills}
        </div>

        <div class="col">
            ${candidate.applied_job?.title || "N/A"}
        </div>

        <div class="col"   ${candidate.score >= 80 ? 'high' :
      candidate.score >= 50 ? 'medium' : 'low'}">
            ${candidate.score ?? 0}
        </div>

    </div>
                `;
            });

            // 🔥 THIS WAS MISSING
            container.innerHTML = html;

        })
        .catch(error => {

            console.log("Error loading candidates:", error);

            document.getElementById("candidateList").innerHTML =
                "<p>Failed to load candidates</p>";
});
}
loadCandidates();  
