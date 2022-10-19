import React, {useState, useEffect} from 'react'
import APIService from '../APIService'
import {useHistory} from 'react-router-dom'
import mainLogo from '../AA.png'
const sty ={    width: '100%',  }
const divStyle = {    width: '25%',    margin: '27px',}

function ClubByCity() {    
    const [City, setCity]= useState('')    
    const [ShowClub, setShowClub]=useState(false)   
    const [Club, setClub]=useState([])   
    let history= useHistory()
    const goHome =() =>{ history.push('/home') }
    
    const findClub = ()=>{        
            setShowClub(false)        
            APIService.ClubCity({'City': City})       
            .then(resp=> setClub(resp))       
            .then(Club.Message==="No Club Exist"? console.log('true'):setShowClub(true))     
            .catch(error => console.log(error)) }

    return (  <div div className='App'>      
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
              <label className='mylabel' htmlFor ="text" >Enter A City Name</label>    
              <br/>        
              <input className='searchbox' type="text"  id= "city" placeholder='City'  value={City} onChange={e => setCity(e.target.value)}/> 
              <br/>  
              <br/> 
              <button style={divStyle} onClick={findClub} className='btn  btn-outline-secondary'> Search</button>      
               {ShowClub===true?      
                <div> 
                {Club.map(c=>{ 
                return(  
                <div className='element' key= {c.Message ? c.Message: c.ClubName}>  
                 {c.Message? 
                  <div>  <br/> <br/> 
                  <h2>{c.Message}</h2>
                  <hr color='black'/> 
                  </div>:
                  <div className='Pl'>
                  <h1 >{c.ClubName}</h1>
                   <hr color='black'/> </div>} 
                   </div> )})} 
                   </div>  :<div> </div> }</div>)}                
        export default ClubByCity
                
