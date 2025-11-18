import React, { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Settings as SettingsIcon, Info } from 'lucide-react'

export default function Settings() {
  const [theme, setTheme] = useState('light')

  return (
    <div className="p-8 space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Settings</h1>
        <p className="text-slate-600">Configure your FileOrganizer preferences</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Appearance</CardTitle>
          <CardDescription>Customize the look and feel</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">Theme</label>
            <div className="flex gap-4">
              <Button
                variant={theme === 'light' ? 'default' : 'outline'}
                onClick={() => setTheme('light')}
              >
                Light
              </Button>
              <Button
                variant={theme === 'dark' ? 'default' : 'outline'}
                onClick={() => setTheme('dark')}
              >
                Dark
              </Button>
              <Button
                variant={theme === 'auto' ? 'default' : 'outline'}
                onClick={() => setTheme('auto')}
              >
                Auto
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>About</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-start gap-4">
            <SettingsIcon className="h-12 w-12 text-blue-500" />
            <div>
              <h3 className="font-semibold text-lg">FileOrganizer Pro</h3>
              <p className="text-sm text-slate-600">Version 1.0.0</p>
              <p className="text-sm text-slate-600 mt-2">
                Intelligent file organization desktop application
              </p>
            </div>
          </div>

          <div className="pt-4 border-t">
            <h4 className="font-semibold mb-2">Features</h4>
            <ul className="space-y-1 text-sm text-slate-600">
              <li>Smart auto-organization with rule engine</li>
              <li>Duplicate file detection and cleanup</li>
              <li>Advanced search capabilities</li>
              <li>Custom tagging system</li>
              <li>File analytics and insights</li>
            </ul>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Database</CardTitle>
          <CardDescription>Manage application database</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="flex items-center gap-4">
            <Info className="h-5 w-5 text-blue-500" />
            <div className="flex-1">
              <p className="text-sm text-slate-600">
                Database location: ~/.fileorganizer/database.db
              </p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
