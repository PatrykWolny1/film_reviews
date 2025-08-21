document.addEventListener('DOMContentLoaded', function () {
  function getCookie(name) {
    return document.cookie.split('; ').find(r => r.startsWith(name + '='))?.split('=')[1];
  }
  function setCookie(name, value, maxAgeSeconds) {
    document.cookie = name + '=' + value + '; path=/; max-age=' + maxAgeSeconds + '; SameSite=Lax';
  }

  const modal = document.getElementById('cookie-modal');
  const overlay = document.getElementById('cookie-overlay');
  const acceptBtn = document.getElementById('accept-cookies');
  const declineBtn = document.getElementById('decline-cookies');

  if (!modal || !overlay || !acceptBtn || !declineBtn) return;

  function showConsent() {
    overlay.hidden = false;
    modal.hidden = false;
    document.body.classList.add('cookie-lock');
  }
  function hideConsent() {
    overlay.hidden = true;
    modal.hidden = true;
    document.body.classList.remove('cookie-lock');
  }

  if (!getCookie('cookie_accepted')) showConsent();

  acceptBtn.addEventListener('click', function () {
    setCookie('cookie_accepted', 'true', 60*60*24*365);
    hideConsent();
  });

  declineBtn.addEventListener('click', hideConsent);
  overlay.addEventListener('click', hideConsent);
});
