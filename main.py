from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fpdf import FPDF
import logging
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PDFGenerator(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Termos de Uso', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        lines = body.split('\n')
        for line in lines:
            if line.startswith("**") and line.endswith("**"):
                self.set_font('Arial', 'B', 12)
                line = line.strip("**")
            else:
                self.set_font('Arial', '', 12)
            self.cell(0, 10, line, ln=True)


@app.post("/term/generate")
def generate_terms(project_name: str = Form(...), contact_email: str = Form(...)):
    try:
        pdf = PDFGenerator()
        pdf.add_page()
        pdf.chapter_title(f"Projeto: {project_name}")
        pdf.chapter_body("Licença: MIT")
        pdf.chapter_body(f"Contato: {contact_email}")

        terms_text = f"""
**TERMOS DE USO**

**1. Aceitação dos Termos**
Ao acessar e usar o aplicativo {project_name}, você concorda em cumprir e estar vinculado aos 
termos e condições descritos neste documento. Se você não concorda com estes termos, 
não deve usar o aplicativo.

**2. Uso do Aplicativo**
Você concorda em usar o aplicativo apenas para fins legais e de acordo com todas as leis e 
regulamentos aplicáveis. Você não deve usar o aplicativo de qualquer maneira que possa 
danificar, desativar, sobrecarregar ou prejudicar os servidores ou redes conectadas ao 
aplicativo.

**3. Propriedade Intelectual**
Todo o conteúdo, incluindo, mas não se limitando a, texto, gráficos, logotipos, ícones, imagens
e software, é propriedade do {project_name} ou de seus licenciadores e está protegido por leis
de direitos autorais e outras leis de propriedade intelectual.

**4. Privacidade**
Sua privacidade é importante para nós. Por favor, revise nossa Política de Privacidade, que 
também rege o uso do aplicativo, para entender nossas práticas.

**5. Limitação de Responsabilidade**
Em nenhuma hipótese o {project_name} será responsável por quaisquer danos indiretos, 
incidentais, especiais, consequenciais ou punitivos decorrentes do uso ou da incapacidade 
de usar o aplicativo.

**6. Segurança**
O {project_name} se compromete a manter medidas de segurança adequadas para proteger suas 
informações pessoais. No entanto, não podemos garantir que terceiros não autorizados nunca 
serão capazes de vencer essas medidas e usar suas informações pessoais de maneira imprópria.

**7. Responsabilidades do Usuário**
Você é responsável por manter a confidencialidade das informações da sua conta, incluindo 
sua senha, e por qualquer atividade que ocorra em sua conta. Você concorda em notificar 
imediatamente o {project_name} sobre qualquer uso não autorizado de sua conta ou qualquer 
outra violação de segurança.

**8. Conteúdo de Terceiros**
O aplicativo pode conter links para sites de terceiros ou serviços que não são de propriedade ou 
controlados pelo {project_name}. O {project_name} não tem controle e não assume responsabilidade 
pelo conteúdo, políticas de privacidade ou práticas de quaisquer sites ou serviços de terceiros.

**9. Rescisão**
Podemos rescindir ou suspender seu acesso ao nosso aplicativo imediatamente, sem aviso 
prévio ou responsabilidade, por qualquer motivo, incluindo, sem limitação, se você violar 
os Termos.

**10. Alterações aos Termos**
O {project_name} reserva-se o direito de modificar estes termos a qualquer momento. 
Quaisquer alterações serão publicadas nesta página e a data da última atualização será 
indicada no topo dos termos.

**11. Indenização**
Você concorda em indenizar, defender e isentar o {project_name} e seus afiliados, diretores, 
funcionários, agentes e licenciadores de todas e quaisquer reivindicações, responsabilidades, 
danos, perdas ou despesas, incluindo honorários advocatícios razoáveis, decorrentes ou 
relacionados ao seu uso ou uso indevido do aplicativo.

**12. Lei Aplicável**
Estes Termos serão regidos e interpretados de acordo com as leis do país em que a sede 
do {project_name} está localizada, sem considerar os conflitos de provisões legais.

**13. Solução de Disputas**
Quaisquer disputas decorrentes ou relacionadas a estes Termos serão resolvidas de forma 
amigável. Se não for possível, as disputas serão submetidas à arbitragem vinculativa na 
jurisdição competente.

**14. Totalidade do Acordo**
Estes Termos constituem o acordo completo entre você e o {project_name} em relação ao uso 
do aplicativo e substituem todos os acordos anteriores ou contemporâneos, comunicações e 
propostas, sejam orais, escritas ou eletrônicas, entre você e o {project_name}.

**15. Divisibilidade**
Se qualquer disposição destes Termos for considerada inválida ou inexequível por um tribunal 
de jurisdição competente, as demais disposições continuarão em pleno vigor e efeito.

**16. Renúncia**
Nenhuma renúncia a qualquer termo destes Termos será considerada uma renúncia adicional ou 
contínua de tal termo ou qualquer outro termo, e a falha do {project_name} em afirmar qualquer 
direito ou disposição sob estes Termos não constituirá uma renúncia a tal direito ou disposição.

**17. Atribuição**
Estes Termos e quaisquer direitos e licenças concedidos aqui não podem ser transferidos ou 
atribuídos por você, mas podem ser atribuídos pelo {project_name} sem restrição.

**18. Notificações**
O {project_name} pode fornecer notificações a você via e-mail, postagem em seu site, ou outros 
meios razoáveis. Qualquer notificação fornecida será considerada entregue e eficaz na data de 
envio ou publicação.

**19. Idioma**
Estes Termos de Uso podem ser traduzidos para outros idiomas. Em caso de conflito entre a 
versão em inglês e a versão traduzida, a versão em inglês prevalecerá.

**20. Relacionamento das Partes**
Você e o {project_name} são contratantes independentes, e nada nestes Termos de Uso cria 
qualquer parceria, joint venture, agência, franquia, relação de trabalho ou de emprego entre 
as partes. Você não tem autoridade para fazer ou aceitar qualquer oferta ou representação em 
nome do {project_name}.

**21. Uso do Aplicativo**
Você concorda em não acessar (ou tentar acessar) qualquer parte do aplicativo por qualquer 
meio que não seja a interface fornecida pelo {project_name}, a menos que você tenha sido 
especificamente autorizado a fazê-lo em um contrato separado com o {project_name}.

**22. Direitos de Propriedade**
Você reconhece e concorda que o {project_name} detém todos os direitos, títulos e interesses 
em e para o aplicativo e seus conteúdos, incluindo todos os direitos de propriedade intelectual.

**23. Ausência de Garantias**
O aplicativo é fornecido "como está" e "como disponível", sem garantias de qualquer tipo, 
expressas ou implícitas, incluindo, mas não se limitando a, garantias de comercialização, 
adequação a um propósito específico, ou não violação.

**24. Exoneração de Responsabilidade**
O {project_name} não garante que o aplicativo será ininterrupto, seguro ou livre de erros. 
Você entende e concorda que você usa o aplicativo por sua conta e risco.

**25. Direitos de Modificação**
O {project_name} se reserva o direito de modificar, suspender ou descontinuar, temporária ou 
permanentemente, o aplicativo ou qualquer serviço fornecido através do aplicativo, com ou 
sem aviso.

**26. Contato**
Para qualquer dúvida, reclamação ou informação adicional sobre estes Termos, por favor, entre 
em contato conosco através do e-mail: {contact_email}.

**27. Atualizações**
É sua responsabilidade revisar regularmente estes Termos para quaisquer alterações. 
Continuação do uso do aplicativo após quaisquer alterações implica na aceitação dos novos 
termos.

**28. Severidade**
Se qualquer disposição destes Termos for considerada inválida ou inexequível, tal disposição 
será limitada ou eliminada na menor medida necessária, de modo que os Termos permaneçam 
em pleno vigor e efeito.

**29. Desistência de Direitos**
Nenhuma disposição destes Termos será considerada uma renúncia a qualquer direito de fazer 
cumprir qualquer disposição desses Termos, a menos que seja feita por escrito e assinada 
por um representante autorizado do {project_name}.
"""
        
        pdf.chapter_body(terms_text.strip())

        output_path = f"{project_name}_terms.pdf"
        pdf.output(output_path)

        return FileResponse(output_path, media_type='application/pdf', filename=output_path)
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn
    logging.info("Starting server...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
