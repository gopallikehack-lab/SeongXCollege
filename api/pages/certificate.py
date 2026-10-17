"""Certificate page template."""

CERTIFICATE_PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Certificate of Completion</title>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@600;800&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<style>
  :root {
    --cert-bg: url('https://i.ibb.co/84b8Y3z9/IMG-20261018-003314.png');
    --cert-top-offset: 32%; 
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background-color: #0f1115; display: flex; flex-direction: column;
    align-items: center; min-height: 100vh; font-family: 'Montserrat', sans-serif;
    padding: 20px; overflow-x: hidden;
  }
  /* PREMIUM PROMPT UI */
  #name-prompt {
    position: fixed; inset: 0; background: rgba(10, 12, 16, 0.85);
    display: flex; align-items: center; justify-content: center;
    z-index: 100; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
    transition: opacity 0.4s ease;
  }
  .prompt-card {
    background: linear-gradient(145deg, rgba(30, 34, 42, 0.9), rgba(18, 20, 26, 0.9));
    border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 24px;
    padding: 40px 30px; width: 90%; max-width: 400px; text-align: center;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    animation: slideUp 0.5s cubic-bezier(0.22, 1, 0.36, 1);
  }
  @keyframes slideUp { from { opacity: 0; transform: translateY(30px) scale(0.95); } to { opacity: 1; transform: translateY(0) scale(1); } }
  .prompt-card h2 { font-weight: 800; font-size: 22px; color: #fff; margin-bottom: 8px; letter-spacing: 0.5px; }
  .prompt-card p { font-size: 13px; color: #8b95a5; margin-bottom: 24px; line-height: 1.5; }
  .input-group { position: relative; margin-bottom: 24px; }
  .input-group input {
    width: 100%; padding: 16px 20px; font-size: 16px; border-radius: 14px;
    border: 2px solid rgba(255, 255, 255, 0.1); background: rgba(0, 0, 0, 0.3);
    color: #fff; font-family: 'Montserrat', sans-serif; font-weight: 600; outline: none;
    transition: all 0.3s ease;
  }
  .input-group input:focus { border-color: #1a4e9e; background: rgba(26, 78, 158, 0.1); box-shadow: 0 0 0 4px rgba(26, 78, 158, 0.2); }
  .prompt-card button {
    width: 100%; padding: 16px; font-size: 15px; font-weight: 800; border-radius: 14px;
    border: none; background: linear-gradient(135deg, #1a4e9e, #4a7cd4); color: #fff;
    cursor: pointer; transition: all 0.3s ease; box-shadow: 0 8px 24px rgba(26, 78, 158, 0.4);
  }
  .prompt-card button:hover { transform: translateY(-2px); box-shadow: 0 12px 28px rgba(26, 78, 158, 0.6); }
  /* CERTIFICATE UI */
  #cert-area { display: none; flex-direction: column; align-items: center; width: 100%; margin-top: 10px; }
  .cert-container {
    position: relative; width: 100%; max-width: 1200px; aspect-ratio: 1.414 / 1; 
    background-image: var(--cert-bg); background-size: cover; background-position: center; background-repeat: no-repeat;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6); overflow: hidden; border-radius: 4px;
  }
  .cert-content {
    position: absolute; inset: 0; display: flex; flex-direction: column;
    align-items: center; padding-top: var(--cert-top-offset); 
  }
  .student-name {
    font-family: 'Dancing Script', cursive; font-size: 4.5vw; color: #1a4e9e; 
    line-height: 1; text-align: center; max-width: 80%; word-wrap: break-word;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.4);
  }
  .cert-details { text-align: center; width: 100%; margin-top: 1.2vw; }
  .success-text { font-size: 1.1vw; color: #444; letter-spacing: 1.5px; margin-bottom: 0.5vw; text-transform: uppercase; font-weight: 600; }
  .course-name { font-size: 1.6vw; font-weight: 800; color: #0b2545; max-width: 80%; margin: 0 auto; line-height: 1.3; }
  /* ACTION BUTTONS */
  .action-bar { margin-top: 24px; display: flex; gap: 16px; flex-wrap: wrap; justify-content: center; }
  .action-bar button {
    padding: 14px 28px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.15);
    background: rgba(255, 255, 255, 0.05); color: #fff; font-size: 14px; font-weight: 600;
    cursor: pointer; display: inline-flex; align-items: center; gap: 8px; transition: all 0.2s ease;
  }
  .action-bar button:hover { background: rgba(255, 255, 255, 0.1); border-color: rgba(255, 255, 255, 0.3); }
  .action-bar button.primary { background: linear-gradient(135deg, #2ecc71, #27ae60); border: none; box-shadow: 0 8px 24px rgba(46, 204, 113, 0.3); }
  .action-bar button.secondary { background: linear-gradient(135deg, #5c8dff, #3b6dff); border: none; box-shadow: 0 8px 24px rgba(92, 141, 255, 0.3); }
  .action-bar svg { width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
  @media (max-width: 768px) {
    .student-name { font-size: 7.5vw; }
    .success-text { font-size: 2.2vw; }
    .course-name { font-size: 3.2vw; }
  }
</style>
</head>
<body>
  <div id="name-prompt">
    <div class="prompt-card">
      <h2>Certificate</h2>
      <p>Enter your full name exactly as it should appear on the certificate.</p>
      <div class="input-group">
        <input type="text" id="user-name-input" placeholder="Your Name" value="__USER_NAME__" autocomplete="off" autofocus>
      </div>
      <button onclick="applyName()">Generate Certificate</button>
    </div>
  </div>

  <div id="cert-area">
    <div class="cert-container" id="certificate">
      <div class="cert-content">
        <div class="student-name" id="display-name"></div>
        <div class="cert-details">
          <div class="success-text">for successfully completing the course of</div>
          <div class="course-name" id="display-course">__COURSE_NAME__</div>
        </div>
      </div>
    </div>
    <div class="action-bar">
      <button class="primary" onclick="downloadPDF()"><svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Download PDF</button>
      <button class="secondary" onclick="downloadImage()"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg> Download Image</button>
    </div>
  </div>
  <script>
    function applyName() {
      const nameInput = document.getElementById('user-name-input').value.trim();
      if (!nameInput) { alert("Please enter your name."); return; }
      document.getElementById('display-name').textContent = nameInput;
      const prompt = document.getElementById('name-prompt');
      prompt.style.opacity = '0';
      setTimeout(() => { prompt.style.display = 'none'; document.getElementById('cert-area').style.display = 'flex'; }, 400);
    }
    document.getElementById('user-name-input').addEventListener('keypress', function (e) { if (e.key === 'Enter') applyName(); });
    async function downloadPDF() {
      const el = document.getElementById('certificate');
      const opt = { margin: 0, filename: 'Certificate.pdf', image: { type: 'jpeg', quality: 1 }, html2canvas: { scale: 2, useCORS: true }, jsPDF: { unit: 'px', format: [1200, 848], orientation: 'landscape' } };
      html2pdf().set(opt).from(el).save();
    }
    async function downloadImage() {
      const el = document.getElementById('certificate');
      const canvas = await html2canvas(el, { scale: 2, useCORS: true });
      const link = document.createElement('a');
      link.download = 'Certificate.png';
      link.href = canvas.toDataURL('image/png');
      link.click();
    }
  </script>
</body>
</html>"""
