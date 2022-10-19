import React, {useState, useEffect} from 'react'
import APIService from '../APIService'
import {useCookies} from 'react-cookie'
import {useHistory} from 'react-router-dom'
import mainLogo from '../AA.png'

const sty ={
    width: '100%',
  }
  const divStyle = {
    width: '25%',
    margin: '27px',
}

function PlyerByCountry() {
    const [Country, setCountry]= useState('')
    const [ShowPlayer, setShowPlayer]=useState(false)
    const [Player, setPlayer]=useState([])


    let history= useHistory()

    const goHome =() =>{
        history.push('/home')
      }

    const FindPlayer = ()=>{
        setShowPlayer(false)
        APIService.PlayerByCountry({'Nationality': Country})
        .then(resp=> setPlayer(resp)) 
        .then(Player.Message==="No Player Exist"? console.log('true'):setShowPlayer(true))
        .catch(error => console.log(error))
    }
  return (
    <div div className='App'>
        <img src={mainLogo} alt='' style={sty}/> 
        <nav>
          <ul>
            <li><button onClick={goHome}>Back To Home</button></li>
          </ul> 
        </nav>
        <br/>

        <br/>
        <br/>
        <br/>
        <br/>

        <label className='mylabel' htmlFor ="text" >Write A Country Name</label> 
        <br/>
        <input className='searchbox' type="text"  id= "country" placeholder='Players Country'
        value={Country} onChange={e => setCountry(e.target.value)}/>

        <button style={divStyle} onClick={FindPlayer} className='btn  btn-outline-secondary'> Search</button>
        {ShowPlayer===true?
        <div>
        {Player.map(p=>{
        return(
          <div className='element' key= {p.Message ? p.Message: [p.Player_Name, p.Season]}>
            
            {p.Message?
            <div>
            <br/>
            <br/>
            <h2>{p.Message}</h2>
            <hr color='black'/>
            </div>:
            <div className='Pl'>
            <h1 >{p.Player_Name}</h1>
            Season :<h1> {p.Season}</h1>
            Club :<h6> {p.P_ClubName}</h6>

            <hr color='black'/>
            </div>}
          </div>
        )
    })}
    </div>
        :<div>
        </div>
        } 
    </div>
  )
}

export default PlyerByCountry