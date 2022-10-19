import React, {useState, useEffect} from 'react'
import APIService from '../APIService'
import {useCookies} from 'react-cookie'
import {useHistory} from 'react-router-dom'
import mainLogo from '../AA.png'

const sty ={
    width: '100%',
  }
const divStyle = {
    margin: '10px',
  };

function Fixtures() {
    const [cookies, setCookie, removeCookie] = useCookies(['Email']);
    const [isShowReview, setShow]= useState(false)
    const [Added, setAdded]= useState('1')
    const [HomeClub, setHomeClub]= useState('')
    const [AwayClub, setAwayClub]= useState('')
    const [Matchdate, setDate]= useState('')
    const [Review, setReview]= useState('')
    const [Rate, setRate]= useState('')
    const [allReviews, setallRev]=useState([])
    const [GoReviews, setGoRevPage]=useState(false)

    let history= useHistory()

    const goHome =() =>{
        history.push('/home')
      }

    useEffect(()=>{
        if(Added==='2'){
          alert("Success Review")
          setAdded('1')
      }else if(Added==='0'){
        alert("Failed Review")
        setAdded('1')
      }
    }, [Added])


    const PostReview = ()=>{
        let email= cookies.Email.toString()
        APIService.writeReview({'UserEmail': email, 'MatchDate':Matchdate, 'Home_ClubName':HomeClub, 
                                'Away_ClubName':AwayClub, 'Rate': Rate,'TextReview': Review})
        .then(resp=> resp.ok===true ? setAdded('2'): setAdded('0'))
        .catch(error => console.log(error))
    }
    const getReviews = ()=>{
        APIService.Get_Reviews({'MatchDate': Matchdate, 'Home_ClubName': HomeClub, 'Away_ClubName':AwayClub})
        .then(resp=> setallRev(resp)) 
        .then(resp=>setGoRevPage(true))
        .catch(error => console.log(error))
    }
    
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
        {GoReviews===false?
        <div>
        <div className='mb-3'>
        {isShowReview ? <h1> Match Reviews </h1>: <h1> Review A Match</h1>}
        </div>
        <div className='mb-3'>
            <label style= {divStyle} htmlFor ="matchdate" className='form-label'>Match Date</label>
            <br/>
            <input style= {divStyle}   type="date" name="matchdate" value={Matchdate} onChange={e => setDate(e.target.value)} />

            <br/>
            <label htmlFor ="homeClub" className='form-label'>Home Club Name</label>
            <br/>
            <select style= {divStyle} name="homeClub" value={HomeClub} onChange={e => setHomeClub(e.target.value)} >
                <optgroup label="Home Club">
                    <option value="AFC Bournemouth">AFC Bournemouth</option>
                    <option value="Arsenal">Arsenal</option>
                    <option value="Aston Villa">Aston Villa</option>
                    <option value="Brentford">Brentford</option>
                    <option value="Brighton and Hove Albion">Brighton and Hove Albion</option>
                    <option value="Burnley">Burnley</option>
                    <option value="Cardiff City">Cardiff City</option>
                    <option value="Chelsea">Chelsea</option>
                    <option value="Crystal Palace">Crystal Palace</option>
                    <option value="Everton">Everton</option>
                    <option value="Fulham">Fulham</option>
                    <option value="Huddersfield Town">Huddersfield Town</option>
                    <option value="Leeds United">Leeds United</option>
                    <option value="Leicester City">Leicester City</option>
                    <option value="Liverpool">Liverpool</option>
                    <option value="Manchester City">Manchester City</option>
                    <option value="Manchester United">Manchester United</option>
                    <option value="Newcastle United">Newcastle United</option>
                    <option value="Norwich City">Norwich City</option>
                    <option value="Sheffield United">Sheffield United</option>
                    <option value="Southampton">Southampton</option>
                    <option value="Tottenham Hotspur">Tottenham Hotspur</option>
                    <option value="Watford">Watford</option>
                    <option value="West Bromwich Albion">West Bromwich Albion</option>
                    <option value="West Ham United">West Ham United</option>
                    <option value="Wolverhampton Wanderers">Wolverhampton Wanderers</option>
                    </optgroup>
                    </select>
                    <br/>
            <br/>
            <label htmlFor ="AwayClub" className='form-label'>Away Club Name</label>
            <br/>
            <select  style= {divStyle} name="AwayClub" value={AwayClub}onChange={e => setAwayClub(e.target.value)} >
                <optgroup label="Away Club">
                    <option value="AFC Bournemouth">AFC Bournemouth</option>
                    <option value="Arsenal">Arsenal</option>
                    <option value="Aston Villa">Aston Villa</option>
                    <option value="Brentford">Brentford</option>
                    <option value="Brighton and Hove Albion">Brighton and Hove Albion</option>
                    <option value="Burnley">Burnley</option>
                    <option value="Cardiff City">Cardiff City</option>
                    <option value="Chelsea">Chelsea</option>
                    <option value="Crystal Palace">Crystal Palace</option>
                    <option value="Everton">Everton</option>
                    <option value="Fulham">Fulham</option>
                    <option value="Huddersfield Town">Huddersfield Town</option>
                    <option value="Leeds United">Leeds United</option>
                    <option value="Leicester City">Leicester City</option>
                    <option value="Liverpool">Liverpool</option>
                    <option value="Manchester City">Manchester City</option>
                    <option value="Manchester United">Manchester United</option>
                    <option value="Newcastle United">Newcastle United</option>
                    <option value="Norwich City">Norwich City</option>
                    <option value="Sheffield United">Sheffield United</option>
                    <option value="Southampton">Southampton</option>
                    <option value="Tottenham Hotspur">Tottenham Hotspur</option>
                    <option value="Watford">Watford</option>
                    <option value="West Bromwich Albion">West Bromwich Albion</option>
                    <option value="West Ham United">West Ham United</option>
                    <option value="Wolverhampton Wanderers">Wolverhampton Wanderers</option>
                    </optgroup>
                    </select>
                    <br/>
        {isShowReview===false? 
            <div className='mb-3'>
            <div>
            <label  htmlFor ="Rate" className='form-label'>Rate</label>
            <br/>
            <select style= {divStyle} name="Rate" value={Rate} onChange={e => setRate(e.target.value)} >
                <optgroup label="Match Rate">
                    <option value="1">1</option>
                    <option value="1.5">1.5</option>

                    <option value="2">2</option>
                    <option value="2.5">2.5</option>

                    <option value="3">3</option>
                    <option value="3.5">3.5</option>

                    <option value="4">4</option>
                    <option value="4.5">4.5</option>

                    <option value="5">5</option>
                    <option value="5.5">5.5</option>

                    <option value="6">6</option>
                    <option value="6.5">6.5</option>

                    <option value="7">7</option>
                    <option value="7.5">7.5</option>

                    <option value="8">8</option>
                    <option value="8.5">8.5</option>

                    <option value="9">9</option>
                    <option value="9.5">9.5</option>

                    <option value="10">10</option>

                    </optgroup>
                    </select>
                    <br/>
            </div>

            <br/>

            <div>
            <label   htmlFor ="review" className='form-label'>Review</label>
            <br/>
            <textarea name="paragraph_text" cols="50" rows="10" value={Review} onChange={e => setReview(e.target.value)}></textarea>
            </div>
            </div>
            :<div></div>}
        </div>
        
        <div className='mb-3'>

        {isShowReview? <button  className='btn  btn-outline-secondary' onClick={getReviews}> Show Reviews</button>
        : <button  className='btn btn btn-outline-secondary' onClick={PostReview}> Submit Review</button>
        }
        </div>
        <div>
            {isShowReview? <h5 style={divStyle}> Write your own Review <br/>  <br/>  <button className='btn btn-outline-secondary btn-lg btn-block' style={divStyle} onClick ={()=>setShow(false)}> Review Match</button> <br/><br/></h5>

        :<div>
        <h5 style={divStyle}> Want to preview others' reviews <br/>  <br/><button className='btn btn-outline-secondary btn-lg btn-block' onClick ={()=>setShow(true)}> Show All Match Reviews</button></h5>
        <br/>
        <br/>
        </div>
        } 

        </div>
    </div>:<div>
        
    {allReviews.map(review=>{
        return(
          <div style={divStyle} key= {review.Message ? review.Message: review.UserEmail}>
            
            {review.Message?
            <div>
            <br/>
            <br/>
            <h2>{review.Message}</h2>
            <hr color='black'/>
            </div>:
            <div text-align='center'>
            <br/>
            <br/>    
            <h5>{review.UserEmail}:</h5>
            <h6>Rate: {review.Rate}</h6>
            <h6>{review.TextReview}</h6>
            <hr color='black'/>
            </div>}
          </div>
        )
    })}
    </div>}
    </div>
  )
}

export default Fixtures