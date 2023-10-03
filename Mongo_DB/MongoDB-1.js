//use("football")

// db.player_detail.insertOne({
//     name: "niraj",
//     country: "argentina",
//     club: "inter miami",
//     age: 36
// })

//db.player_detail.find({})

// db.player_detail.insertMany([
// {
//     name: "luca modric",
//     country: "croatia",
//     club: "real madrid",
//     age: 38
// },
// {
//     name: "harry kane",
//     country: "england",
//     club: "bayern munich",
//     age: 30
// },
// {
//     name: "erling haaland",
//     country: "norwey",
//     club: "man city",
//     age: 23
// },
// {
//     name: "kaliyan mbappe",
//     country: "france",
//     club: "psg",
//     age: 24
// },
// {
//     name: "gavi",
//     country: "spain",
//     club: "fcbarcelona",
//     age: 20
// }
// ])

// db.player_detail.find({})

// db.player_detail.find({country: "argentina"})

// db.player_detail.insertOne({
//     name: "niraj",
//     famous_name: "the goat"
// })

// db.player_detail.find({})

// db.player_detail.find({name: "niraj"})

// db.player_detail.findOne({name: "niraj"})

// db.player_detail.find({}).limit(2)

// db.player_detail.find({}).skip(2)

// db.player_detail.find({}, {name: 1, country: 1})

// db.player_detail.find({}, {name: 1, country: 1, age: 0})

// db.player_detail.find({}).count()

// db.player_detail.find({}).sort({age:1})

// db.player_detail.find({}).sort({age:-1})

// db.player_detail.find({ age: { $gt: 24 } })

// db.player_detail.find({ age: { $gte: 24 } })

// db.player_detail.find({ age: { $lt: 30 } })

// db.player_detail.find({ age: { $lte: 30 } })

// db.player_detail.find({ age: { $lte: 30 } }).count()

// db.player_detail.aggregate([
//     { $limit: 2 }
//   ])

// db.player_detail.aggregate([
//     { $skip: 1 }
//   ])

// db.player_detail.aggregate([
//     { $project: { name: 1, age: 1, _id: 0} }
//   ])

// db.player_detail.aggregate([
//     { $sort: { age: 1 } }
//   ])

// db.player_detail.aggregate([
//     { $sort: { age: -1 } }
//   ])

// db.player_detail.aggregate([
//     { $match: { age: { $gt: 30 } } }
//   ])

// db.player_detail.aggregate([
//     { $match: { age: { $gte: 30 } } }
//   ])

// db.player_detail.aggregate([
//     { $match: { age: { $lt: 30 } } }
//   ])

// db.player_detail.aggregate([
//     { $match: { age: { $lte: 30 } } }
//   ])

// db.player_detail.aggregate([
//     {
//       $group: {
//         _id: "$gender",
//         totalAge: { $sum: "$age" },
//         averageAge: { $avg: "$age" }
//       }
//     }
//   ])

// db.player_detail.updateOne(
//     { famous_name: "the goat" },    
//     { $set: { other_name: "the greatest" } }
//   )

// db.player_detail.updateOne(
//     { name: "erling haaland" },   
//     { $set: { age: 22 } }
//   )

// db.player_detail.updateMany(
//     { name: "lionel messi" },    
//     { $set: { favourite_player: "diego maradona" } }
//   )

// db.player_detail.updateMany(
//     { name: "lionel messi" },   
//     { $set: { name: "lionel andres messi" } }
//   )

// db.player_detail.updateMany(
//     { name: "erling haaland" },
//     { $inc: { age: 1 } }
//   )

// db.player_detail.updateMany(
//     { name: "harry kane" },
//     { $inc: { age: -1 } }
//   )

// db.player_detail.updateMany(
//     { },
//     { $set: { current_status: "actively playing" } }
//   )

// db.player_detail.updateMany(
//     {},
//     { $unset: { club: "" } }
//   )

// db.player_detail.updateMany(
//     { name: "harry kane" },
//     { $push: { club: "bayern munich" } }
//   );

// db.player_detail.updateMany(
//     { name: "harry kane" },
//     { $set: { hobby: "gardening" } }
//   );

// db.player_detail.deleteOne(
//     { name: "luca modric" }
//   );

// db.player_detail.deleteOne(
//     { _id: ObjectId("650ca2ef5fc5737a9c46bfb5") }
//   )

// db.player_detail.deleteMany({
//     _id: { $in: [ObjectId("650ca2ef5fc5737a9c46bfb3"), ObjectId("650ca2ef5fc5737a9c46bfb4")] }
//   })

// db.player_detail.deleteMany({
//     name: { $in: ["lionel andres messi", "harry kane"] }
//   })

// db.player_detail.insertMany([
//    {
//     name: "niraj",
//     country: "argentina",
//     club: "inter miami",
//     age: 36
// },
// {
//     name: "luca modric",
//     country: "croatia",
//     club: "real madrid",
//     age: 38
// },
// {
//     name: "harry kane",
//     country: "england",
//     club: "bayern munich",
//     age: 30
// },
// {
//     name: "erling haaland",
//     country: "norwey",
//     club: "man city",
//     age: 23
// },
// {
//     name: "kaliyan mbappe",
//     country: "france",
//     club: "psg",
//     age: 24
// },
// {
//     name: "gavi",
//     country: "spain",
//     club: "fcbarcelona",
//     age: 20
// },
// {
//     name: "niraj",
//     famous_name: "the goat"
// }
// ])

// db.player_detail.deleteMany({
//     name: "niraj" 
//   })

// db.player_detail.deleteMany(
//     { age: { $gte: 30 } }
//   )

// db.player_detail.deleteMany({})

// db.player_detail.drop()

// db.player_detail.find({})
