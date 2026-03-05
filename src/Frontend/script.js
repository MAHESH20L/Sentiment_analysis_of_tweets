let globalData = null;

// ================= UPLOAD =================
async function uploadCSV(){

    const fileInput = document.getElementById("csvFile");
    const file = fileInput.files[0];

    if(!file){
        alert("Upload CSV first");
        return;
    }

    document.getElementById("loading").style.display="block";

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/predict-csv",{
        method:"POST",
        body:formData
    });

    const data = await res.json();
    globalData = data;

    document.getElementById("loading").style.display="none";

    buildTable();      // default visible
    buildCharts();     // for charts + pdf
    buildReco();       // recommendations
}

// ================= TABLE DEFAULT =================
function buildTable(){

    let html=`<div class="section-card">
    <h2>📄 Sentiment Results</h2>
    <table>
    <tr>
    <th>Tweet</th>
    <th>Topic</th>
    <th>Sentiment</th>
    <th>Confidence</th>
    </tr>`;

    globalData.results.forEach(r=>{
        html+=`<tr>
        <td>${r.tweet}</td>
        <td>${r.topic}</td>
        <td>${r.sentiment}</td>
        <td>${r.confidence}</td>
        </tr>`;
    });

    html+="</table></div>";

    document.getElementById("tableSection").innerHTML = html;
}

// ================= CHARTS + PDF CONTENT =================
function buildCharts(){

    let html = `
    <div class="section-card" id="pdfContent">

    <h1 style="text-align:center;">AI Sentiment Analysis Report</h1>

    <!-- ===== CHARTS FIRST ===== -->
    <h2>📊 Overall Sentiment</h2>
    <img src="data:image/png;base64,${globalData.overall_sentiment_chart}">

    <h2>📊 Topic-wise Sentiment</h2>
    <img src="data:image/png;base64,${globalData.topic_sentiment_chart}">

    <!-- ===== RECOMMENDATIONS ===== -->
    <h2>🧠 AI Recommendations</h2>
    `;

    globalData.recommendations.forEach(r=>{
        html += `<p>👉 ${r}</p>`;
    });

    // ===== TABLE LAST =====
    html += `
    <h2>📄 Sentiment Results</h2>
    <table border="1" style="width:100%;border-collapse:collapse;">
    <tr>
    <th>Tweet</th>
    <th>Topic</th>
    <th>Sentiment</th>
    <th>Confidence</th>
    </tr>`;

    globalData.results.forEach(r=>{
        html += `<tr>
        <td>${r.tweet}</td>
        <td>${r.topic}</td>
        <td>${r.sentiment}</td>
        <td>${r.confidence}</td>
        </tr>`;
    });

    html += `</table></div>`;

    document.getElementById("chartSection").innerHTML = html;
}

// ================= RECOMMENDATIONS (NAV VIEW) =================
function buildReco(){

    let html = `<div class="section-card"><h2>🧠 AI Recommendations</h2>`;

    globalData.recommendations.forEach(r=>{
        html += `<p>👉 ${r}</p>`;
    });

    html += "</div>";

    document.getElementById("recoSection").innerHTML = html;
}

// ================= NAVIGATION =================
function showHome(){
    document.getElementById("chartSection").style.display="none";
    document.getElementById("recoSection").style.display="none";
    document.getElementById("tableSection").style.display="block";
}

function showCharts(){
    document.getElementById("chartSection").style.display="block";
    document.getElementById("recoSection").style.display="none";
    document.getElementById("tableSection").style.display="none";
}

function showReco(){
    document.getElementById("chartSection").style.display="none";
    document.getElementById("recoSection").style.display="block";
    document.getElementById("tableSection").style.display="none";
}

// ================= PDF DOWNLOAD =================
function downloadPDF(){

    const element = document.getElementById("pdfContent");

    if(!element){
        alert("Upload CSV first");
        return;
    }

    html2pdf().from(element).save("AI_Sentiment_Report.pdf");
}
