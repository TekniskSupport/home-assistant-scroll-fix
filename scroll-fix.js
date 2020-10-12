(function () {
  let injectedStyle = document.createElement('style');
  injectedStyle.appendChild(document.createTextNode('body { overflow: hidden scroll; }'));
  document.querySelector('head').appendChild(injectedStyle);
  window.setInterval(() => {{
    if(!document.querySelector('body').style.overflowY !== 'scroll') {{
      document.querySelector('body').style.overflowX='hidden';
      document.querySelector('body').style.overflowY='scroll';
    }}
  }}, 10000);
})();
