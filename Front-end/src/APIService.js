
export default class APIService {

  static LoginUser(body) {

    return fetch('http://127.0.0.1:8000/User/LogIn', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)

    }).then(resp => resp.json())

  }
  static RegisterUser(body) {

    return fetch('http://127.0.0.1:8000/User/Register', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)

    }).then(resp => resp['status'])

  }

  static writeReview(body){
    return fetch('http://127.0.0.1:8000/Reviews/set', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)

      }).then(resp => resp)
  }
  static Get_Reviews(body){
    return fetch('http://127.0.0.1:8000/Reviews/get', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)

      }).then(resp => resp.json())
  }
  static PlayerByName(body){
    return fetch('http://127.0.0.1:8000/Player/byname', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)

      }).then(resp => resp.json())
  }
  static PlayerByPos(body){
    return fetch('http://127.0.0.1:8000/Player/byposition', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)

      }).then(resp => resp.json())
  }
  static PlayerByCountry(body){
    return fetch('http://127.0.0.1:8000/Player/bycountry', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)

      }).then(resp => resp.json())
  }
  static ClubByName(body){
    return fetch('http://127.0.0.1:8000/Club/byname', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)
      }).then(resp => resp.json())
  }
  static ClubCity(body){
    return fetch('http://127.0.0.1:8000/Club/bycity', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)
      }).then(resp => resp.json())
  }
  static ClubStad(body){
    return fetch('http://127.0.0.1:8000/Club/bystadium', {
      'method':'POST',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)
      }).then(resp => resp.json())
  }
  static MostSeasonWin(body){
    return fetch('http://127.0.0.1:8000/TopTeams/mostwinseason', {
      'method':'GET',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)
      }).then(resp => resp.json())
  }
  static TotalWon(body){
    return fetch('http://127.0.0.1:8000/TopTeams/mostwin', {
      'method':'GET',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)
      }).then(resp => resp.json())
    }

  static TotalHomeWon(body){
        return fetch('http://127.0.0.1:8000/TopTeams/mosthomewin', {
          'method':'GET',
          headers: {
              'Content-Type':'application/json',
            }, 
            body:JSON.stringify(body)
          }).then(resp => resp.json())
  }
  static YellowCards(body){
    return fetch('http://127.0.0.1:8000/TopTeams/mostyellow', {
      'method':'GET',
      headers: {
          'Content-Type':'application/json',
        }, 
        body:JSON.stringify(body)
      }).then(resp => resp.json())
}
static Fouls(body){
  return fetch('http://127.0.0.1:8000/TopTeams/mostfouls', {
    'method':'GET',
    headers: {
        'Content-Type':'application/json',
      }, 
      body:JSON.stringify(body)
    }).then(resp => resp.json())
}
static Shots(body){
  return fetch('http://127.0.0.1:8000/TopTeams/mostshots', {
    'method':'GET',
    headers: {
        'Content-Type':'application/json',
      }, 
      body:JSON.stringify(body)
    }).then(resp => resp.json())
}
}