import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 587  
EMAIL_SERVER = "smtp.gmail.com"  # Adjust server address, if you are not using @outlook

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(subject, receiver_email, name, attachment_path):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Bullseye to Success UTM", f"{sender_email}"))
    msg["To"] = receiver_email

    msg.set_content(
        f"""\
        Salam sejahtera Tuan/Puan,

        Saya Pua Zhi Ying dari ULRF-2672 (01), UTM, penganjur program memanah Bullseye to Success yang diadakan di Pusat Rekreasi Tampok Laut pada 6 Januari 2024 lalu. Dengan ini saya sertakan sijil penyertaan kepada {name} atas penglibatan beliau dalam program kami.

        Kami amat menghargai kerjasama dan dedikasi yang diberikan oleh tuan/puan sepanjang program kami. Diharapkan tuan/puan dapat meneruskan minat dalam sukan memanah dan berjaya pada masa akan datang.

        Sekian, terima kasih.
        """
    )
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Salam sejahtera Tuan/Puan,</p>
        <p>Saya Pua Zhi Ying dari ULRF-2672 (01), UTM, penganjur program memanah Bullseye to Success yang diadakan di Pusat Rekreasi Tampok Laut pada 6 Januari 2024 lalu. Dengan ini saya sertakan sijil penyertaan kepada <strong>{name}</strong> atas penglibatan beliau dalam program kami.</p>
        <p>Kami amat menghargai kerjasama dan dedikasi yang diberikan oleh tuan/puan sepanjang program kami. Diharapkan tuan/puan dapat meneruskan minat dalam sukan memanah dan berjaya pada masa akan datang.</p>
        <p>Sekian, terima kasih.</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            file_data = attachment.read()
            file_name = os.path.basename(attachment_path)
            msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


def get_file_names(folder_path):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder path '{folder_path}' does not exist.")
        return []

    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Filter out non-files (directories, etc.)
    files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]

    # Remove the suffix from file names
    files_without_suffix = [os.path.splitext(file)[0] for file in files if file.endswith('.pdf')]

    return files_without_suffix

sijil_type = "pencapaian" #or penyertaan, for cert file directory
names = get_file_names(sijil_type)

emails_pencapaian = {
    "ANDIK MUHAMMAD NAJMI BIN E RAZALI": None,
    "DAING MUHAMMAD ABDUH BIN DAING MUHAMAD AZMI": "abdjalilbalkis@gmail.com",
    "FATHIYAHTUL HUSNA BINTI MOHD JOHARI": "abdjalilbalkis@gmail.com",
    "ILHAM AISYAH BINTI BAHTIAR": "abdjalilbalkis@gmail.com",
    "MUHAMMAD ANIQ ANAQI BIN OTHMAN": "anaqi.aniq@icloud.com",
    "MUHAMMAD IRHAS BIN BACHOK": None,
    "NAWAL BUTHAINAH BINTI DAING MUHAMAD AZMI": "nawalbuthainah09@gmail.com",
    "NUR AFIAH BINTI DAENG ABD JAMAL": "abdjalilbalkis@gmail.com",
    "NUR ALEEYA SAFFIYA BINTI DEDY CHANDRA": "nassaffiya@gmail.com",
    "NUR IZZAH BADRINA BINTI SAAD": "Badrinaizzah07@yahoo.com",
    "RIFQI RAZIN BIN ROZAKI": "agropanthera@gmail.com",
    "RUSYDINA AISYAH BINTI ROBZI": "rohanimahs@yahoo.com",
    "SYAHIDAH AZRIMAH BINTI ABDUL AZIZ": "syahidah0729@gmail.com"
}

emails_penyertaan = {
    "AMMAR HUSAINI BIN SUDIRMAN": "guruakauntdi@gmail.com",
    "ANDIK MUHAMMAD NAJMI BIN E RAZALI": None,
    "AYU KHADEEJAH BINTI HATIM": "rahayuabdmanan@yahoo.com",
    "DAING MUHAMMAD ABDUH BIN DAING MUHAMAD AZMI": "abdjalilbalkis@gmail.com",
    "FATHIYAHTUL HUSNA BINTI MOHD JOHARI": "abdjalilbalkis@gmail.com",
    "ILHAM AISYAH BINTI BAHTIAR": "abdjalilbalkis@gmail.com",
    "KAISYA LUTHFIYAH BT JAFARUDIN": None,
    "MAIMANAH LABIIBAH BINTI SADINI": None,
    "MUHAMAD BASYAR IRFAN BIN MOHD BAHRI": "bakhtiariqbalbahri@gmail.com",
    "MUHAMAD THSAQIF HAFIZI BIN MUHAMADIN": "puspa_nida@yahoo.com.my",
    "MUHAMMAD ABROOR SYARIFF BIN HJ SADINI": None,
    "MUHAMMAD ANIQ ANAQI BIN OTHMAN": "anaqi.aniq@icloud.com",
    "MUHAMMAD IRHAS BIN BACHOK": None,
    "MUHAMMAD NASR KHWARIZMI BIN MOHD RAHMAT": "nasr080824@gmail.com",
    "MUHAMMAD THAQIF AMSYAR BIN MUHAMMAD NUR": "yatieduasa@gmail.com",
    "NAWAL BUTHAINAH BINTI DAING MUHAMAD AZMI": "nawalbuthainah09@gmail.com",
    "NUR AFIAH BINTI DAENG ABD JAMAL": "abdjalilbalkis@gmail.com",
    "NUR AIMY NAZURAH BINTI ZAINOOR": "zainoor1979@gmail.com",
    "NUR ALEEYA SAFFIYA BINTI DEDY CHANDRA": "nassaffiya@gmail.com",
    "NUR BATRISYIA BINTI JAFARUDIN": None,
    "NUR IZZAH BADRINA BINTI SAAD": "Badrinaizzah07@yahoo.com",
    "PUSPA NIDA TARUBUS": None,
    "RIFQI RAZIN BIN ROZAKI": "agropanthera@gmail.com",
    "RUSYDINA AISYAH BINTI ROBZI": "rohanimahs@yahoo.com",
    "SYAHIDAH AZRIMAH BINTI ABDUL AZIZ": "syahidah0729@gmail.com"
}
    
if __name__ == "__main__":

    for peserta_name in names:
        if peserta_name in emails_pencapaian:
            if emails_pencapaian[peserta_name]:
                send_email(
                    subject="Sijil Pencapaian Program Memanah Bullseye to Success",
                    name=peserta_name,
                    receiver_email=emails_pencapaian[peserta_name],
                    attachment_path=f"{sijil_type}/{peserta_name}.pdf",
                )


#    for peserta_name in names:
#         if peserta_name in emails_penyertaan:
#             if emails_penyertaan[peserta_name]:
#                 send_email(
#                     subject="Sijil Penyertaan Program Memanah Bullseye to Success",
#                     name=peserta_name,
#                     receiver_email=emails_penyertaan[peserta_name],
#                     attachment_path=f"{sijil_type}/{peserta_name}.pdf",
#                 )
