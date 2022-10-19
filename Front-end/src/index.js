import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Route, BrowserRouter} from 'react-router-dom';
import {CookiesProvider} from 'react-cookie';
import Login from './components/Login';
import Fixtures from './components/Fixtures';
import PlayerByName from './components/PlayerByName';
import PlayerByPos from './components/PlayerByPos';
import PlyerByCountry from './components/PlayerByCountry';
import ClubName from './components/ClubName';
import ClubByCity from './components/ClubByCity';
import ClubStadium from './components/ClubStadium';
import WonSeason from './components/WonSeason';
import TotalWins from './components/TotalWins';
import TotalHomeWins from './components/TotalHomeWins';
import MostYellow from './components/MostYellow';
import MostFouls from './components/MostFouls';
import MostShots from './components/MostShots';

function Router() {
   
  return(
    <CookiesProvider>
    <BrowserRouter>

    <Route exact path = "/" component = {Login}/>
    <Route exact path = "/home" component = {App}/>
    <Route exact path = "/fixtures" component = {Fixtures}/>
    <Route exact path = "/player/byname" component = {PlayerByName}/>
    <Route exact path = "/player/byposition" component = {PlayerByPos}/>
    <Route exact path = "/player/bycountry" component = {PlyerByCountry}/>
    <Route exact path = "/club/byname" component = {ClubName}/>
    <Route exact path = "/club/bycity" component = {ClubByCity}/>
    <Route exact path = "/club/bystadium" component = {ClubStadium}/>
    <Route exact path = "/topteams/1" component = {WonSeason}/>
    <Route exact path = "/topteams/2" component = {TotalWins}/>
    <Route exact path = "/topteams/3" component = {TotalHomeWins}/>
    <Route exact path = "/topteams/4" component = {MostYellow}/>
    <Route exact path = "/topteams/5" component = {MostFouls}/>
    <Route exact path = "/topteams/6" component = {MostShots}/>



    </BrowserRouter>
    </CookiesProvider>
  )

}


ReactDOM.render(
  <React.StrictMode>
    <Router />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
