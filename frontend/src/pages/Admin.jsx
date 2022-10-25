import React,{useState,useEffect} from 'react'
import { AdminMid } from '../components/admin/AdminMid'
import { Navbar } from '../components/navbar/Navbar'
import { menu } from '../components/Data'
import { ListItems } from '../components/admin/ListItems'
import { Modal } from '../components/modal/Modal'

export const Admin = ({userId,isOpen,setIsOpen,setUserId}) => {
  console.log(isOpen)
  const [category,setCategory] = useState("Main")
  const [items,setItems] = useState(menu)

  useEffect(() => {
    setItems(category === "Main" ? menu : menu.filter((item) => item.category === category))
  },[category])

  return (
    <>
      {isOpen === 'open' && <Modal setIsOpen={setIsOpen} setUserId={setUserId}/>}
      <div className="table-top">
        <Navbar userId={userId} setIsOpen={setIsOpen}/>
        <AdminMid setCategory={setCategory}/>
      </div>
      <div className="table-bottom admin-bottom w-1/2 mt-10 mx-auto">
          {items?.map((item) => (
            <ListItems
              key={item.id}
              title={item.title}
              category={item.category}
              price={item.price}
              cal={item.cal}
              img={item.img}
              desc={item.desc}
            />
          ))}
      </div>
    </>
  )
}
