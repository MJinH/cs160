import React from 'react'

export const ListItems = ({title,category,price,cal,img,desc}) => {

    return (
        <div className="item-container w-full my-6 h-52 flex relative">
            <div className="item-left w-4/12 h-full box-border overflow-hidden">
                <img src={img} className="item-img w-full h-full rounded-md"></img>
            </div>
            <div className="item-right flex flex-col justify-between p-4">
                <div>
                    <h2 className="text-lg font-bold">{title}</h2>
                    <span className="font-light">{cal}</span>
                </div>
                <div className="flex">
                    <span className="item-price font-bold">{`$${price}`}</span>
                    <span className="absolute right-7">ICON</span>
                </div>
            </div>
        </div>
    )
}
