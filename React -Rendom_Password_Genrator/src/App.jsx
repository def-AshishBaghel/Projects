import React, { useRef } from "react";
import "./App.css";
import { useState } from "react";
import { useCallback } from "react";
import { useEffect } from "react";

export default function App() {
  const [lenght, setLenght] = useState(8);
  const [allownum, setAllownum] = useState(true);
  const [allowword, setAllowword] = useState(true);
  const [password, SetPassword] = useState("");


  const PasswordRef = useRef(null)

  const copytext = useCallback(()=>{
       window.navigator.clipboard.writeText(password)
       PasswordRef.current.select()
       
  },[password])
  const passwordgenrator = useCallback(() => {
    let pass = "";
    let str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    if (allownum) {
      str += "0123456789";
    }
    if (allowword) {
      str += "@#$%^&*(){}:':>?/<";
    }
    for (let i = 0; i <= lenght; i++) {
      let rand = Math.floor(Math.random() * str.length);
      pass += str.charAt(rand);
    }
    SetPassword(pass);
  }, [lenght, allownum, allowword]);

  useEffect(() => {
    passwordgenrator();
  }, [passwordgenrator]);

  return (
    <>
     <h1>Rendom Password Genrator</h1>
      <div className="box">
        <div className="in">
          <input
            className="val"
            type="text"
            value={password}
            onChange={(e) => {
              SetPassword(e.target.value);
            }}
            placeholder="Password"
            readOnly
          />
          <button className="btn" onClick={copytext}>Copy</button>
        </div>
        <div className="check">
          <input
            type="range"
            min={8}
            max={50}
            value={lenght}
            onChange={(e) => {
              setLenght(e.target.value);

            }}
            ref={PasswordRef}
          />
          <label>Lenght({lenght})</label>
          <input
            type="checkbox"
            defaultChecked={allownum}
            onChange={() => {
              setAllownum((prev) => !prev);
            }}
          />

          <label>Number</label>
          <input
            type="checkbox"
            defaultChecked={allowword}
            onChange={() => {
              setAllowword((prev) => !prev);
            }}
          />
          <label>Keywords</label>
        </div>
      </div>
    </>
  );
}
