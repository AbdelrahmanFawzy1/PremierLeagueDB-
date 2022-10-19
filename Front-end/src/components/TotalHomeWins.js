import React, {useState, useEffect} from 'react'
import APIService from '../APIService'
import {useHistory} from 'react-router-dom'
import mainLogo from '../AA.png'
const sty ={    width: '100%',  }
const divStyle = { width: '25%', margin: '27px',}

function TotalHomeWins() {    
    const [Club, setClub]=useState([])   
    let history= useHistory()
    const goHome =() =>{ history.push('/home') }
    
    const findClub = ()=>{        
            APIService.TotalHomeWon()       
            .then(resp=> setClub(resp))       
            .catch(error => console.log(error)) }

    useEffect(() => {
                findClub()
              }, []);

    return (         

            <div className='App'>     
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
              <label className='mylabel' htmlFor ="text" >The Most Home Winning Clubs In Total</label>    
              <br/>        
                {Club.map(c=>{ 
                return(  
                <div className='new_elem'key= {c.Club}>  
                <h1 >{c.Club}</h1>
                Wins: <h6>{c.WinningGames}</h6> 
                <hr color='black'/> </div>)})}
                   </div>  ) }               
        export default TotalHomeWins
            