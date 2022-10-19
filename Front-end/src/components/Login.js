import React, {useState, useEffect} from 'react'
import APIService from '../APIService'
import {useCookies} from 'react-cookie'
import {useHistory} from 'react-router-dom'
import mainLogo from '../A1.jpg'

const divStyle = {
    margin: '10px',
  };
const sty ={
  width: '100%',
}


function Login() {
  const [email, setEmail]=useState('')
  const [username, setUsername]= useState('')
  const [password, setPassword]= useState('')
  const [birthdate, setDate]= useState('')
  const [Gender, setGender]= useState('')
  const [Club, setClub]= useState('')
  const [status, setCookies, removeCookie] = useCookies(["mystatus"]);  
  const [Acc, setAcc] = useCookies(["Email"]);
  const[isLogin, setLogin]= useState(true)

  let history= useHistory()


  
  useEffect(()=>{
      if(status["mystatus"]==='202'){
        setAcc(["Email"], email)
        history.push('/home')
      }
      else if(status["mystatus"]==='403'){
        alert("Make Sure Your Email and Password are Correct")
        removeCookie('mystatus')
    }
  }, [status])
  const signinBtn = ()=>{
      APIService.LoginUser({'UserEmail': email, 'Password': password})
      .then(resp=> setCookies(["mystatus"],resp[1]['status']) )
      .catch(error => console.log(error))
  }

const RegisterBtn = ()=>{
    APIService.RegisterUser({'UserEmail': email, 'UserName':username, 'Gender':Gender, 'DateOfBirth':birthdate, 'FavouriteClubName': Club,
                             'Password': password})
      .then(()=>signinBtn())
      .catch(error => console.log(error))
}
  return (
    <div className='mb-2'> 

        <div className='Img'>
        <img src={mainLogo} style={sty} height="700" alt='Welcome To Premier League'/>    
        </div>  

        <br/>
        <div className='mb-2'>
        {isLogin ? <h1> Sign In </h1>: <h1> Register</h1>}
        </div>

        {isLogin===false? 
            <div className='mb-2'>
            <label htmlFor ="text" className='form-label'>User Name</label> 
            <input type="text" className='form-control' id= "username" placeholder='User Name'
            value={username} onChange={e => setUsername(e.target.value)}
        />
            </div>
            :<div></div>
            }

        <div className='mb-2'>
            <label htmlFor ="Email Address" className='form-label'>Email Address</label>
            <input type="email" className='form-control' id= "Email" placeholder='Email Address'
            value={email} onChange={e => setEmail(e.target.value)}
            />

        </div>

        <div className='mb-2'>
            <label htmlFor ="password" className='form-label'>Password</label>
            <input type="password" className='form-control' id= "password" placeholder='Password'
            value={password} onChange={e => setPassword(e.target.value)}
            />

        </div>


        {isLogin===false? 
            <div>

            <div>
            <label style= {divStyle} htmlFor ="gender" className='form-label'>Gender</label>
            <br/>
            <input style= {divStyle}   type="radio" name="gender" value="M" onChange={e => setGender(e.target.value)} /> Male
            <input style= {divStyle}   type="radio" name="gender" value="F" onChange={e => setGender(e.target.value)}/> Female
            </div>

            <br/>

            <div>
            <label style= {divStyle} htmlFor ="birthdate" className='form-label'>Date Of Birth</label>
            <br/>
            <input style= {divStyle}   type="date" name="birthdate" value={birthdate} onChange={e => setDate(e.target.value)} />
            </div>

            <br/>
            <div>
            <label style= {divStyle} htmlFor ="favoriteclub" className='form-label'>Favorite Club</label>
            <br/>
            <select style= {divStyle} name="club" onChange={e => setClub(e.target.value)} >
                <optgroup label="Clubs">
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

            </div>

            </div>
            :<div></div>
            }

        <div className='mb-2'>

        {isLogin? <button onClick={signinBtn} className='btn  btn-outline-secondary'> Sign In</button>
        : <button onClick={RegisterBtn} className='btn btn btn-outline-secondary'> Register</button>
        }

        </div>

        <div className='mb-2'>
            {isLogin? <h5> Don't have an account, <br/>  <br/>  <button className='btn btn-outline-secondary btn-lg btn-block' onClick ={()=>setLogin(false)}> Register</button> <br/><br/></h5>
            
        :<h5> Already have an account, <br/>  <br/><button className='btn btn-outline-secondary btn-lg btn-block' onClick ={()=>setLogin(true)}> Sign In</button> <br/> <br/></h5>
        } 

        </div>
    </div>
  )
}

export default Login