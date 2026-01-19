import streamlit as st

texto_utilizado = st.text_input("Enter your text to transform in text modified")

SendButton = st.button("send")


MAPA_SMALL_CAPS = {
    "a": "ᴀ",
    "b": "ʙ",
    "c": "ᴄ",
    "d": "ᴅ",
    "e": "ᴇ",
    "f": "ꜰ",
    "g": "ɢ",
    "h": "ʜ",
    "i": "ɪ",
    "j": "ᴊ",
    "k": "ᴋ",
    "l": "ʟ",
    "m": "ᴍ",
    "n": "ɴ",
    "o": "ᴏ",
    "p": "ᴘ",
    "q": "ǫ",   
    "r": "ʀ",
    "s": "ꜱ",
    "t": "ᴛ",
    "u": "ᴜ",
    "v": "ᴠ",
    "w": "ᴡ",
    "x": "x",   
    "y": "ʏ",
    "z": "ᴢ",

    "A": "ᴀ",
    "B": "ʙ",
    "C": "ᴄ",
    "D": "ᴅ",
    "E": "ᴇ",
    "F": "ꜰ",
    "G": "ɢ",
    "H": "ʜ",
    "I": "ɪ",
    "J": "ᴊ",
    "K": "ᴋ",
    "L": "ʟ",
    "M": "ᴍ",
    "N": "ɴ",
    "O": "ᴏ",
    "P": "ᴘ",
    "Q": "ǫ",
    "R": "ʀ",
    "S": "ꜱ",
    "T": "ᴛ",
    "U": "ᴜ",
    "V": "ᴠ",
    "W": "ᴡ",
    "X": "x",
    "Y": "ʏ",
    "Z": "ᴢ",
}






def aplicar_estilo(texto_original, mapa_de_letras):
    texto_estilizado = ""

    for caractere in texto_original:
        if caractere in mapa_de_letras:
            texto_estilizado += mapa_de_letras[caractere]
        else:
            texto_estilizado += caractere
    return texto_estilizado

if SendButton:
    resultado = aplicar_estilo(
    texto_utilizado,
    MAPA_SMALL_CAPS
    )

    st.text("Aqui está seu texto modificado:")
    st.code(resultado)