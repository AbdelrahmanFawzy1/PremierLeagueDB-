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

function PlayerByPos() {
    const [Position, setPosition]= useState('')
    const [ShowPlayer, setShowPlayer]=useState(false)
    const [Player, setPlayer]=useState([])


    let history= useHistory()

    const goHome =() =>{
        history.push('/home')
      }

    const FindPlayer = ()=>{
        setShowPlayer(false)
        APIService.PlayerByPos({'PlayingPosition': Position})
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

        <label className='mylabel' htmlFor ="text" >Select A Playing Position</label> 
        <br/>

        <select className='searchbox' style= {divStyle} name="Position" value={Position} onChange={e => setPosition(e.target.value)} >
                <optgroup label="Player Position">
                    <option value="Goalkeeper">Goalkeeper</option>
                    <option value="Defender">Defender</option>
                    <option value="Midfielder">Midfielder</option>
                    <option value="Forward">Forward</option>
                    </optgroup>
                    </select>
        <button style={divStyle} onClick={FindPlayer} className='btn  btn-outline-secondary'> Search</button>
        {ShowPlayer===true?
        <div>
        {Player.map(p=>{
        return(
          <div className='element' key= {p.Message ? p.Message: [p.PlayerName, p.DateOfBirth]}>
            
            {p.Message?
            <div>
            <br/>
            <br/>
            <h2>{p.Message}</h2>
            <hr color='black'/>
            </div>:
            <div className='Pl'>
            <h1 >{p.PlayerName}</h1>
            Date Of Birth: <h6>{p.DateOfBirth}</h6>
            Country: <h6>{p.Nationality}</h6>
            Weight (KG):<h6> {p.Weight}</h6>
            Height (CM):<h6> {p.Height}</h6>
            PlayingPosition:<h6> {p.PlayingPosition}</h6>
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

export default PlayerByPos