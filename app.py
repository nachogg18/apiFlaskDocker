from flask import Flask,jsonify,request


app = Flask(__name__)

from pieces import pieces

@app.route("/pieces/",methods = ['GET'])
def get_pieces():
    return jsonify({"message":pieces})

@app.route("/pieces/<string:piece_name>/",methods = ['GET'])
def get_piece(piece_name):
    pieces_found = [piece for piece in pieces if piece["name"] == piece_name]
    if len(pieces_found) > 0:
        return jsonify({"piece": pieces_found[0]})
    return jsonify({"piece":"not found"})

 
@app.route("/pieces/",methods=['POST'])
def addPiece():
    newPiece = {
        "name": request.json["name"],
        "value" : request.json["value"]
    }
    pieces.append(newPiece)
    return jsonify({"message":"Piece added","pieces":pieces})


if __name__ == '__main__':
    app.run(debug=True,port=4000)

