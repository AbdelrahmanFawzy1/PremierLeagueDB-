import React, {useState, useEffect} from 'react'
import APIService from '../APIService'
import {useHistory} from 'react-router-dom'
import mainLogo from '../AA.png'
const sty ={    width: '100%',  }
const divStyle = {    width: '25%',    margin: '27px',}

function MostFouls() {    
    const [Club, setClub]=useState([])   
    let history= useHistory()
    const goHome =() =>{ history.push('/home') }
    
    const findClub = ()=>{        
            APIService.Fouls()       
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
              <label className='mylabel' htmlFor ="text" >The Clubs with the most Fouls</label>    
              <br/>        
                {Club.map(c=>{ 
                return(  
                <div className='new_elem'key= {c.Club}>  
                <h1 >{c.Club}</h1>
                Fouls Number: <h6>{c.FoulsNumber}</h6> 
                <hr color='black'/> </div>)})}
                   </div>  ) }               
        export default MostFouls
            