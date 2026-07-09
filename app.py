import streamlit as st
import time

# 1. ตั้งค่าหน้าตาของเว็บแอปพลิเคชัน
st.set_page_config(page_title="ร้านคอมช่างแจ้", page_icon="💻")

# ==========================================
# 🌟 ส่วนที่เพิ่มเข้ามาใหม่: แสดงรูปป้ายร้าน
# ==========================================
try:
    # เปลี่ยน "shop.png" เป็นชื่อไฟล์รูปของคุณที่อัปโหลดลง GitHub (เช่น "banner.jpg")
    st.image("shop.png", use_container_width=True) 
except:
    # ถ้าพิมพ์ชื่อรูปผิด หรือหารูปไม่เจอ ระบบจะขึ้นข้อความนี้แทนเว็บพัง
    st.warning("⚠️ ยังไม่ได้ใส่รูปป้ายร้าน หรือพิมพ์ชื่อรูปผิดครับ")

st.title("💻 ร้านซ่อม/จำหน่ายอุปกรณ์คอมพิวเตอร์ ช่างแจ้")

# 2. ตั้งค่าคำถาม-คำตอบ 
FAQ_RESPONSES = {
    "เปิด": "ร้านเปิดให้บริการทุกวัน จันทร์-เสาร์ เวลา 09.00 น. - 20.00 น. ครับ (หยุดทุกวันอาทิตย์) ⏰",
    "คิว": "ตอนนี้คิวซ่อมไม่เยอะครับ ช่างแจ้เคลียร์งานไว หากเอาเครื่องเข้ามาเช็กวันนี้ สามารถรับกลับได้เลยภายในช่วงเย็นครับ 🛠️",
    "เถื่อน": "ต้องขออภัยด้วยครับ ทางร้านรับลงเฉพาะ Windows แท้และโปรแกรมลิขสิทธิ์เท่านั้นครับผม เพื่อความปลอดภัยของข้อมูลลูกค้าครับ 🛡️",
    "เกม": "มีครับผม! คอมพิวเตอร์ประกอบสำหรับเล่นเกมงบประหยัด เริ่มต้นที่ 12,000 บาท เล่นเกมฮิตๆ ได้ลื่นไหลแน่นอน ทักมาคุยสเปกกันก่อนได้ครับ 🎮",
    "แฟลชไดร์ฟ": "แฟลชไดร์ฟมีหลายความจุเลยครับ เริ่มต้น 32GB ราคา 150 บาท และ 64GB ราคา 250 บาท ของแท้รับประกันตลอดอายุการใช้งานครับ 💾",
    "ครูแจ้": "สวัสดีครับ ผมแจ้ คนหล่อหน้าตาดี ตัวตึงสายคอนเท้น" 
}

# 3. สร้างระบบจดจำประวัติการแชต
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "สวัสดีครับ ร้านคอมช่างแจ้ยินดีให้บริการ! สอบถามเรื่องเวลาเปิดร้าน, คิวซ่อม, จัดสเปกคอม หรือซื้ออุปกรณ์ ทักถามบอตได้เลยครับ 🤖"}
    ]

# แสดงประวัติแชตเก่า
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. ฟังก์ชันทำเอฟเฟกต์ค่อยๆ พิมพ์ตอบกลับ (Streaming)
def simulate_streaming(text):
    for char in text:
        yield char
        time.sleep(0.02) 

# 5. รับข้อความจากผู้ใช้
if prompt := st.chat_input("พิมพ์คำถามของคุณที่นี่... (ลองพิมพ์คำว่า 'ครูแจ้')"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 6. ค้นหาคำตอบจากคำสำคัญ
    bot_reply = "ขออภัยครับ บอตไม่เข้าใจในคำถามนะครับ รบกวนพิมพ์คำถามใหม่ หรือทิ้งเบอร์โทรไว้ให้ช่างติดต่อกลับนะครับ 🙏"
    
    for keyword, response in FAQ_RESPONSES.items():
        if keyword in prompt:
            bot_reply = response
            break

    # 7. แสดงข้อความของ AI พร้อมเอฟเฟกต์พิมพ์
    with st.chat_message("assistant"):
        response_text = st.write_stream(simulate_streaming(bot_reply))
        
    st.session_state.messages.append({"role": "assistant", "content": response_text})
