// ==UserScript==
// @name         Nexus Auto Download
// @match        https://www.nexusmods.com/*/mods/*?tab=files&file_id=*
// @grant        window.close
// ==/UserScript==

/* Polls the page for the 'Slow Download' button, clicks it, 
   and closes the tab after a delay to allow the nxm protocol to fire.
*/
const checkInterval = setInterval(() => {
    const slowBtn = document.getElementById('slowDownloadButton');
    if (slowBtn) {
        slowBtn.click();
        clearInterval(checkInterval);
        setTimeout(() => window.close(), 8000);
    }
}, 1000);