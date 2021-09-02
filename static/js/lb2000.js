window.onload = function () {
  console.log(summonerid)
  loadmatches()
  console.log('done')

  document.getElementById("champion_masteryBtn").onclick = function () {
    var element = document.getElementsByClassName(summonerid);
    console.log("elemment len:"+ element.length)
    console.log("button clicked")
    if (document.getElementById("masterydiv").style.overflow == "hidden") {
      document.getElementById("masterydiv").style.overflow = "visible";
      document.getElementById("masterydivtext").innerHTML = "Hide";
    } else {
      document.getElementById("masterydiv").style.overflow = "hidden";
      document.getElementById("masterydivtext").innerHTML = "Show all";
    }
  }

};;

function showplayer() {
  var element = document.getElementsByClassName(summonerid);
  for (i=0; i< element.length; i++) {
    element[i].style.display = 'block';
    element[i].parentElement.style.float = 'left';
    //element[i].parentElement.parentElement.parentElement.style.color match element
  }
};

function loadmatches() {
  var ancestor = document.getElementById('match_history');
  var childNodes = ancestor.getElementsByTagName('*');
  var i, e, d;
  for (i = 0; i < childNodes.length; ++i) {
    gameid = String(childNodes[i].id).split('_');
    path = 'static/lolgames_html/'+gameid[0] + '/' + gameid[1] + '.txt'
    //console.log(path, childNodes[i].id)
    e = childNodes[i];
    //console.log("new match")
    while (true) {
      var breakCondition = checkFileExist(path);
      //console.log("found file:", breakCondition)
      if (breakCondition) {            
          break;
      }
      sleep(1000);
    }
    //console.log('made it here')
    loadDoc(path,e);
    showplayer();
  
    
    e.innerHTML = path;
    };
}

function loadDoc(path, e) {
  //console.log(path)
  var xhttp = new XMLHttpRequest();
  xhttp.addEventListener('load', showplayer);
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      e.innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", path, true);
  xhttp.send();
}

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e8; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function checkFileExist(urlToFile) {
  var xhr = new XMLHttpRequest();
  xhr.open('HEAD', urlToFile, false);
  xhr.send();
   
  if (xhr.status == "404") {
      return false;
  } else {
      return true;
  }
}

function settingsBtn(id, default_on){
  element = document.getElementById(id)
  console.log("color: ", element.style.color)
  if (element.style.color == 'var(--main-color)'){
    element.style.color = 'var(--error-color)';
    var element = document.getElementsByClassName(id);
    for (i=0; i< element.length; i++) {
      element[i].style.display = 'none';
    }
  }
  else if(element.style.color == 'var(--error-color)'){
    console.log('not red')
    element.style.color = 'var(--main-color)';
    var element = document.getElementsByClassName(id);
    for (i=0; i< element.length; i++) {
      element[i].style.display = '';
  }}
  else{
    if(default_on){
      element.style.color = 'var(--error-color)';
      var element = document.getElementsByClassName(id);
      for (i=0; i< element.length; i++) {
        element[i].style.display = 'none';
      }
    }
    else{
      element.style.color = 'var(--main-color)';
      var element = document.getElementsByClassName(id);
      for (i=0; i< element.length; i++) {
        element[i].style.display = '';

    }}
  }
  console.log('button pressed', id)
}