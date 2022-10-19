import './App.css';
import React from 'react'
import {useState, useEffect} from 'react'
import {useCookies} from 'react-cookie'
import mainLogo from './AA.png'
import {useHistory} from 'react-router-dom'
import EPLLogo from './EPL.jpg'

const sty ={
  width: '100%',
}


function App() {
  const [status, setStatus, removeCookie]= useCookies(['mystatus'])

  let history= useHistory()

  useEffect(()=>{
    if(!status['mystatus'])
        history.push('/')
  },[status])
  

  const logoutBtn =() => {
    removeCookie('csrftoken')
    removeCookie('mystatus')
    removeCookie('Email')

  }
 
  const goMatch =() =>{
    history.push('/fixtures/')
  }

  const goHome =() =>{
    history.push('/home')
  }



  const goPlayer =() =>{
    history.push('/player/byname')
  }
  const goPlayerbyPos =() =>{
    history.push('/player/byposition')
  }
  const goPlayerbycountry =() =>{
    history.push('/player/bycountry')
  }
  const goClub =() =>{
    history.push('/club/byname')
  }
  const goClubCity =() =>{
    history.push('/club/bycity')
  }
  const goClubStad =() =>{
    history.push('/club/bystadium')
  }
  const goTopTeams1 =() =>{
    history.push('/topteams/1')
  }
  const goTopTeams2 =() =>{
    history.push('/topteams/2')
  }
  const goTopTeams3 =() =>{
    history.push('/topteams/3')
  }

  const goTopTeams4 =() =>{
    history.push('/topteams/4')
  }
  const goTopTeams5 =() =>{
    history.push('/topteams/5')
  }
  const goTopTeams6 =() =>{
    history.push('/topteams/6')
  }
  return(

    <div className='App'>

        <img src={mainLogo} alt='' style={sty}/>  
        <div className='nav'>
        <nav>
          <ul>
            <li><button onClick={goHome}>Home</button></li>
            <li><button onClick={goMatch}>Match Reviews</button></li>
            <li><button onClick={goPlayer}>Players</button>
              <ul>
              <li><button  onClick={goPlayer}> Player By Name</button>  </li>
              <li><button   onClick={goPlayerbyPos}> Player By Position</button>  </li>
              <li><button   onClick={goPlayerbycountry}> Player By Country</button>  </li>
              </ul>
            </li>
            <li><button onClick={goClub}>Clubs</button> 
            <ul>
              <li><button onClick={goClub}  > Club By Name</button>  </li>
              <li><button  onClick={goClubCity}> Club By City</button>  </li>
              <li><button  onClick={goClubStad}> Club By Stadium</button>  </li>
              </ul>
            </li>

            <li><button onClick={goTopTeams1}>Top Teams</button> 
              <ul>
                <li><button  onClick={goTopTeams1}> Most Matches Won By Season</button>  </li>
                <li><button  onClick={goTopTeams2}> Most Total Matches Won</button>  </li>
                <li><button  onClick={goTopTeams3} > Most Total Home Matches Won</button>  </li>
                <li><button  onClick={goTopTeams4} > Most Total Yellow Cards</button>  </li>
                <li><button  onClick={goTopTeams5}> Most Total Fouls</button>  </li>
                <li><button  onClick={goTopTeams6}> Most Total Shots</button>  </li>
              </ul>
            </li>
            <li><button onClick={logoutBtn} > SIGN OUT</button>  </li>
          </ul>
        </nav>
        </div>  
        <img src={EPLLogo} alt='Welcome To The Unofficial Premier League Website' style={sty}/>  
    </div>

  );
}

export default App;