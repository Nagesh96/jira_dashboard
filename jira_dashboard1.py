from jira import JIRA

# Connecting to your Jira instance
jira = JIRA(server='YOUR_JIRA_SERVER', basic_auth=('YOUR_USERNAME', 'YOUR_PASSWORD'))

# Define the dashboard name and create it
dashboard_name = 'MyDashboard'
dashboard = jira.create_dashboard(dashboard_name)

# Define the JQL query with the specific version
version_to_display = '1.0'
jql_query = f'project = XYZ AND fixVersion = "{version_to_display}"'

# Add gadgets to the dashboard using the specified filter query
filter_gadget_params = {
    'filterId': None,  # Will be replaced with the actual filter ID
    'jql': jql_query
}

# Creating a filter first and obtaining its ID
new_filter = jira.create_filter('Filter for Version 1.0', jql_query)
filter_gadget_params['filterId'] = new_filter.id

# Adding the filter results gadget to the dashboard using the filter query
jira.add_gadget_to_dashboard(dashboard.id, 'filter-results-gadget', filter_gadget_params)

print(f"Dashboard '{dashboard_name}' created successfully!")
