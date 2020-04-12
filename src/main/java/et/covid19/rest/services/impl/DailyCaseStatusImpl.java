package et.covid19.rest.services.impl;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import et.covid19.rest.annotations.EthLoggable;
import et.covid19.rest.dal.model.CaseStat;
import et.covid19.rest.dal.repositories.DailyStatusRepository;
import et.covid19.rest.services.IDailyCaseStatus;
import et.covid19.rest.swagger.model.ModelDailyCaseStatus;
import et.covid19.rest.swagger.model.ModelDailyCaseStatusList;
import et.covid19.rest.util.GeneralUtils;
import et.covid19.rest.util.exception.EthException;
import et.covid19.rest.util.exception.EthExceptionEnums;
import et.covid19.rest.util.mappers.DailyStatusMapper;

@Service
public class DailyCaseStatusImpl implements IDailyCaseStatus {

	@Autowired
	private DailyStatusRepository dailyStatusRepository;
	
	@Override
	@EthLoggable
	public ModelDailyCaseStatus getDailyCaseStatus(LocalDate reportingDate) throws EthException {
		try {
			LocalDate repDate = reportingDate !=null ? reportingDate : LocalDate.now();
			CaseStat stat = dailyStatusRepository.findByReportDate(repDate)
					.stream().findFirst()
					.orElseThrow(EthExceptionEnums.DAILY_STAT_NOT_FOUND);
			
			return DailyStatusMapper.INSTANCE.entityToDto(stat);
		} catch (Exception ex) {
			throw ex;
		}
	}

	@Override
	@EthLoggable
	public ModelDailyCaseStatusList getAllDailyCaseStatus() throws EthException {
		try {
			List<CaseStat> stat = dailyStatusRepository.findAll();
			ModelDailyCaseStatusList dailies = new ModelDailyCaseStatusList();
			stat.stream().forEach(val -> {
				dailies.addListItem(DailyStatusMapper.INSTANCE.entityToDto(val));
			});
			return dailies;
		} catch (Exception ex) {
			throw ex;
		}
	}

	@Override
	@EthLoggable
	public boolean addDailyStatus(ModelDailyCaseStatus model) throws EthException {
		try {
			if(!GeneralUtils.validateNumericValues(Arrays.asList(
					model::getCriticalCases,
					model::getNewCases,
					model::getNewDeaths,
					model::getRecovered,
					model::getNewTests))) 
				throw EthExceptionEnums.VALIDATION_EXCEPTION.get();
			
			CaseStat lastStatusData = dailyStatusRepository.findLastUpdated();
			
			CaseStat newStat = DailyStatusMapper.INSTANCE.dtoToEntity(model.reportDate(LocalDate.now()));
			if(lastStatusData != null) {
				newStat.setSeriousCriticalCases(Integer.sum(model.getCriticalCases(), lastStatusData.getSeriousCriticalCases()));
				newStat.setTotalCases(Integer.sum(model.getNewCases(), lastStatusData.getTotalCases()));
				newStat.setTotalDeaths(Integer.sum(model.getNewDeaths(), lastStatusData.getTotalDeaths()));
				newStat.setTotalRecovered(Integer.sum(model.getRecovered(), lastStatusData.getTotalRecovered()));
				newStat.setTotalTests(Integer.sum(model.getNewTests(), lastStatusData.getTotalTests()));
				
				Integer active = lastStatusData.getActiveCases() + model.getNewCases();
				active = active - model.getNewDeaths() - model.getRecovered();
				if(Integer.signum(active) == -1) 
					throw EthExceptionEnums.VALIDATION_EXCEPTION.get();
				
				newStat.setActiveCases(active);
			}
			
			dailyStatusRepository.save(newStat);
			return true;
		} catch (Exception ex) {
			throw ex;
		}
	}

}