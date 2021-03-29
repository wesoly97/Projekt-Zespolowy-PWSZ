import React, { useState, useEffect } from 'react';

export default function Test(){

    const [currentSet, setCurrentSet] = useState([]);
    const getSets=async()=>{
      const res=await fetch('http://127.0.0.1:5000/index2')
      const data=await res.json();
      console.log(data)
      setCurrentSet(data);

    }
  useEffect(()=>{
    getSets();
  },[])

    return(
      <div>

{
					currentSet.map((item, i) => {
						return (
							<div key={i}>
                <h1>{item.zestaw.pytanie1.tresc}</h1>
							</div>
						);
					})
				}
  </div>
    );
}