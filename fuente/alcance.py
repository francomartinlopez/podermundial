# Alcance efectivo (no legal): dónde puede actuar de verdad cada actor (17 de noviembre de 2026).
# G = en cualquier parte del mundo; R = en un grupo de países o una región; N = solo dentro de un país.
# Valores para la fórmula del puntaje final: global 0,60, regional 0,25, nacional 0,15.

VALOR = {"G": .60, "R": .25, "N": .15}
NOMBRE = {"G": "Global", "R": "Regional (un grupo de países)", "N": "Nacional"}

GLOBAL = set("""
casablanca kremlin consejoestado
pentagono epl ffaa_rusia ffaa_francia ffaa_reinounido socom cmc
cia nsa mss mossad gru svr mi6 gchq dgse rgb u8200 nro dia odni
sinaloa cjng ndrangheta isis
pcch
saud alnahyan althani maktoum porsche_se
musk ellison thiel bezos zuckerberg arnault
amazon alphabet microsoft apple nvidia openai palantir tsmc huawei alibaba nso foxconn asml sap
jpmorgan goldman blackrock vanguard statestreet berkshire spglobal moodys hsbc softbank brookfield blackstone kkr apollo
allianz axa mufg bnp_paribas deutsche barclays santander pif nbim qia temasek cic gpif cdb lloyds
meta bytedance x telegram
glencore exxon shell bp totalenergies aramco rosatom vitol jbs cargill riotinto vale trafigura bhp cnpc chevron
chinarareearth mitsui
spacex samsung vw airbus mitsubishi toyota boeing tata siemens catl inditex lvmh byd hyundai basf sony
lockheed northrop rtx gendyn casc bae thales norinco safran l3harris huntington
fed bpi
pfizer bayer lilly
doj
santasede sud opusdei
tesoro_eeuu city_londres congreso_eeuu ufwd bis acp mofcom
fifa coi
deloitte mckinsey
visa mastercard swift iso icann euroclear
reuters nyt newscorp bbc xinhua disney economist bertelsmann
otan bm fmi oms csonu opep omc
armadores_gr
gates wef osf wellcome
msc maersk cosco dpworld cmport
harvard mit stanford oxford
bilderberg trilateral
""".split())

REGIONAL = set("""
gob_india lider_iran comisioneu
fdi ejercito_pak ffaa_india tsk ffaa_egipto jsdf bundeswehr ffaa_corea adf ffaa_ucrania epc
isi raw mois irgc_io gur mit_tr bnd nis_corea sbu gip pla_ib
cgri quds fsb mps_china fbi
pcc cv prince clan_golfo trenaragua sunyeeon los_lobos
hezbola hutis africacorps pmf jnim eln hamas alshabaab m23 let
ptk
erdogan lula zelenski kadyrov netanyahu aliyev kagame lukashenko
walton koch bollore exor wallenberg luksic al_sabah rothschild quandt schwarz koc
m_ambani g_adani timchenko
anduril safaricom smic leidos
icbc sberbank vtb boc itau btg novo_fundacion
tencent
gazprom stategrid edf rosneft petrobras sinopec eni petronas ocp sonatrach fonterra kazatomprom nornickel lukoil novatek cnnc orano
reliance adani techint dangote
cetc elbit baykar dassault rostec iai avic rafael rheinmetall hanwha navalgroup
bce boe boj pboc
tjue cpi
hawza_najaf patriarcado hermandad alazhar lmm
doe sasac consejo_seg_rusia oficina39 prop_pcch
boozallen
cips
aljazeera rt comcast
aes ocs brics
cfr rand brookings aipac chatham
cas tsinghua
ugle
""".split())

from nucleo3 import ALC_G as _G3, ALC_R as _R3
GLOBAL |= _G3; REGIONAL |= _R3 - _G3
from nucleo4 import ALC_G as _G4, ALC_R as _R4
GLOBAL |= _G4; REGIONAL |= _R4 - _G4
from nucleo5 import ALC_G as _G5, ALC_R as _R5
GLOBAL |= _G5; REGIONAL |= _R5 - _G5
from revision import A_GLOBAL as _AG, A_NACIONAL as _AN
REGIONAL -= _AG | _AN
GLOBAL = (GLOBAL | _AG) - _AN
assert not GLOBAL & REGIONAL, GLOBAL & REGIONAL


def alcance(i):
    return "G" if i in GLOBAL else "R" if i in REGIONAL else "N"
