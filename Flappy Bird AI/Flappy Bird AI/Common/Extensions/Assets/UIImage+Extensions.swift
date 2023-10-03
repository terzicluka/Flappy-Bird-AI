//
//  UIImage+Extensions.swift
//  Flappy Bird AI
//
//  Created by Terzić Luka on 03.10.2023..
//

import UIKit

extension UIImage {
    
    enum FlappyBird {
        enum Background {
            static let backgroundBase = UIImage(named: "Background/BackgroundBase")!
            static let backgroundDay = UIImage(named: "Background/BackgroundDay")!
        }
        
        enum Bird {
            static let blueBirdDownFlap = UIImage(named: "Bird/BlueBirdDownFlap")!
            static let blueBirdMidFlap = UIImage(named: "Bird/BlueBirdMidFlap")!
            static let blueBirdUpFlap = UIImage(named: "Bird/BlueBirdUpFlap")!
        }
        
        enum Pipe {
            static let greenPipe = UIImage(named: "Pipe/GreenPipe")!
        }
        
        enum Messages {
            static let gameOver = UIImage(named: "Messages/GameOver")!
            static let startGame = UIImage(named: "Messages/StartGame")!
        }
        
        enum Numbers {
            static let zero = UIImage(named: "Numbers/Zero")!
            static let one = UIImage(named: "Numbers/One")!
            static let two = UIImage(named: "Numbers/Two")!
            static let three = UIImage(named: "Numbers/Three")!
            static let four = UIImage(named: "Numbers/Four")!
            static let five = UIImage(named: "Numbers/Five")!
            static let six = UIImage(named: "Numbers/Six")!
            static let seven = UIImage(named: "Numbers/Seven")!
            static let eight = UIImage(named: "Numbers/Eight")!
            static let nine = UIImage(named: "Numbers/Nine")!
        }
    }
}
